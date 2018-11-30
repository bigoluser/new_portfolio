from django.db import models
from django.utils import timezone

class Contact(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=25)
  email = models.EmailField()
  message = models.TextField()
  date = models.DateField(default=timezone.now)
