from django.db import models
from category.models import Category
from django.utils.timezone import now

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=200)
    book_isbn = models.CharField(max_length=13, unique=True)
    book_author = models.CharField(max_length=100)
    book_total_copies = models.IntegerField()
    book_available_copies = models.IntegerField()
    book_desc = models.TextField()
    book_image = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    borrowing_period = models.IntegerField(default=7)
    book_date_added = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.book_title