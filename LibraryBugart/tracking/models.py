from django.db import models
from books.models import Book
from departments.models import Department
from patron.models import Patron
from django.utils import timezone

class Tracking(models.Model):
    tracking_number = models.CharField(max_length=20, unique=True, blank=True, null=True)

    # Foreign keys
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)  # This links the patron
    patron_fname = models.CharField(max_length=100)
    patron_lname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    patron_dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    patron_type = models.CharField(max_length=50)

    request_book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Book being tracked
    request_status = models.CharField(max_length=20)
    patron_due_date = models.DateField(null=True, blank=True)  # Due date for returning the book

    def save(self, *args, **kwargs):
        # Generate tracking number if it doesn't exist
        if not self.tracking_number:
            self.tracking_number = self.generate_tracking_number()

        super().save(*args, **kwargs)

    def generate_tracking_number(self):
        # Get patron type prefix
        patron_type_map = {
            'Student': 'A',
            'Faculty': 'B',
            'Employee': 'C'
        }

        patron_type_prefix = patron_type_map.get(self.patron_type, 'A')  # Default to 'A' if not found

        # Format the current date as ddmmyyyy
        date_str = timezone.now().strftime('%d%m%Y')

        # Get the sequential number for the given date (reset every day)
        sequence_number = self.get_sequence_number(date_str)

        # Combine all parts to form the tracking number
        tracking_number = f"{patron_type_prefix}{date_str}{sequence_number:02d}"
        
        return tracking_number

    def get_sequence_number(self, date_str):
        # Find the most recent tracking number for the given date
        last_tracking = Tracking.objects.filter(tracking_number__startswith=date_str).order_by('-tracking_number').first()

        # If no previous tracking number exists for this date, start from 1
        if last_tracking:
            last_sequence = int(last_tracking.tracking_number[8:])  # Get the last sequence number
            return last_sequence + 1
        else:
            return 1

    def __str__(self):
        return f"Tracking #{self.tracking_number} for {self.patron_fname} {self.patron_lname}"
