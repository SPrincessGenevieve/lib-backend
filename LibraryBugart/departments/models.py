from django.db import models
from django.utils.timezone import now

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_title = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return self.dept_title