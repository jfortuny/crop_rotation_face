from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    user_id = models.BigIntegerField(blank=True,null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    canSMS = models.BooleanField(default=True)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True, null=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        contact_text = self.name + " - " + self.subject
        return contact_text
