from django.db import models
from django.utils import timezone
from departments.models import Department
from datetime import timedelta
from books.models import Book

from django.core.exceptions import ValidationError

class Patron(models.Model):
    REQUEST_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Overdue', 'Overdue'),
        ('Returned', 'Returned'),
    ]
    
    PATRON_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
        ('Employee', 'Employee'),
    ]

    request_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)  # Book being borrowed
    book_borrowing_period = models.IntegerField(null=True, blank=True)  # Borrowing period in days
    patron_id_number = models.CharField(max_length=100)  # Removed unique=True
    patron_id = models.AutoField(primary_key=True)
    patron_type = models.CharField(max_length=50, choices=PATRON_TYPE_CHOICES, default='Student')
    
    patron_fname = models.CharField(max_length=100)
    patron_lname = models.CharField(max_length=100)
    patron_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    patron_email = models.EmailField()  # Removed unique=True to allow repeated emails
    patron_contact_no = models.CharField(max_length=15)
    date_added = models.DateField(default=timezone.now, blank=True)
    
    patron_approved_date = models.DateField(null=True, blank=True)
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='Pending')
    patron_due_date = models.DateField(null=True, blank=True)  # Due date for returning the book
    overdue_days = models.IntegerField(default=0)

    def calculate_overdue_days(self):
        if self.patron_due_date and self.request_status != 'Returned':
            today = timezone.now().date()
            if today > self.patron_due_date:
                self.overdue_days = (today - self.patron_due_date).days
            else:
                self.overdue_days = 0
        else:
            self.overdue_days = 0

    def clean(self):
        """Auto-fill fields if patron_id_number already exists."""
        if Patron.objects.filter(patron_id_number=self.patron_id_number).exists():
            existing_patron = Patron.objects.get(patron_id_number=self.patron_id_number)
            self.patron_type = existing_patron.patron_type
            self.patron_fname = existing_patron.patron_fname
            self.patron_lname = existing_patron.patron_lname
            self.patron_dept = existing_patron.patron_dept
            self.patron_email = existing_patron.patron_email
            self.patron_contact_no = existing_patron.patron_contact_no
        super().clean()

    def save(self, *args, **kwargs):
        # Import Tracking here to avoid circular import
        from tracking.models import Tracking
        
        previous_status = None
        if self.pk:
            previous_status = Patron.objects.get(pk=self.pk).request_status

        self.calculate_overdue_days()

        today = timezone.now().date()
        
        if self.request_status != 'Pending' and self.patron_approved_date is None:
            self.patron_approved_date = today

        if self.request_status == 'Approved' and self.patron_approved_date:
            if self.request_book:
                self.book_borrowing_period = self.request_book.borrowing_period
            self.patron_due_date = self.patron_approved_date + timedelta(days=self.book_borrowing_period)

            if self.request_book and self.request_book.book_available_copies > 0:
                self.request_book.book_available_copies -= 1
                self.request_book.save()
            elif self.request_book and self.request_book.book_available_copies <= 0:
                raise ValueError("No available copies left to borrow")

        if self.request_status == 'Returned' and previous_status != 'Returned':
            if self.request_book:
                self.request_book.book_available_copies += 1
                self.request_book.save()

        super().save(*args, **kwargs)

        # Create or update the Tracking record whenever the Patron's record is saved
        Tracking.objects.update_or_create(
            patron=self,  # Foreign key reference to the Patron
            request_book=self.request_book,  # Foreign key to the borrowed book
            defaults={
                'patron_fname': self.patron_fname,
                'patron_lname': self.patron_lname,
                'id_number': self.patron_id_number,
                'patron_dept': self.patron_dept,
                'patron_type': self.patron_type,
                'request_status': self.request_status,
                'patron_due_date': self.patron_due_date,
            }
        )

    def __str__(self):
        return f"{self.patron_fname} {self.patron_lname}"
