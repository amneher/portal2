from django.db import models

# Create your models here.
class File(models.Model):
    description = models.CharField(max_length=255, blank=False)
    file_dump = models.FileField(upload_to='media/')
    upload_date = models.DateTimeField(auto_now_add=True)
    

class Customer(models.Model):
    name = models.CharField(blank=False)
    company = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)