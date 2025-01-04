from django.db import models
from django.utils.timezone import now

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=100)
    category_date_added = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.category_title