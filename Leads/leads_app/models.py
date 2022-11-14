from django.db import models
from django.utils import timezone

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=220,default='')
    email = models.EmailField(max_length=220,default='')
    date_subscribed = models.DateTimeField(default=timezone.now)

class Contact(models.Model):
    name = models.CharField(max_length=220,default='')
    email = models.EmailField(max_length=220,default='')
    subject = models.CharField(max_length=60,default='')
    message = models.TextField(max_length=5000,default='')
    contact_date = models.DateTimeField(default=timezone.now)

