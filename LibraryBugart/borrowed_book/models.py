from django.db import models
from datetime import timedelta
from books.models import Book
from patron.models import Patron

class BorrowedBook(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)  # Due date based on borrowing period

    def save(self, *args, **kwargs):
        if not self.due_date:
            # Calculate due date based on the book's borrowing period
            self.due_date = self.borrow_date + timedelta(days=self.book.borrowing_period)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.book_title} borrowed by {self.patron.patron_fname} {self.patron.patron_lname}"
