from django.db import models

# Create your models here.
class File(models.Model):
    file_dump = models.FileField(upload_to='media/')
    

class Customer(models.Model):
    name = models.CharField(blank=False)
    company = models.CharField()
    account = models.CharField()
    email = models.CharField()
    address = models.CharField()
    is_active = models.BooleanField()