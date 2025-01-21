from django.db import models
from django.utils.timezone import now

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    profile_image = models.TextField()
    creation_date = models.DateTimeField(default=now, editable=False)
    password = models.CharField(max_length=200)
    
    def __str__(self):
            return f"{self.last_name}, {self.first_name}"