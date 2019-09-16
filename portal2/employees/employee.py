from django.db import models

from . import Position

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    phone = models.CharField()
    address = models.TextArea()
    birthdate = models.CharField()
    hire_date = models.DateTimeField()
    left_date = models.DateTimeField()
    status_choices = [
        ('PT', 'Part-Time'),
        ('FT', 'Full-Time'),
        ('TM', 'Temporary'),
        ('CT', 'Contract'),
    ]
    status = models.CharField(max_length=2, choices=status_choices, default='PT')
    rfid = models.CharField()
    hrid = models.CharField()
    is_employed = models.BooleanField()
    is_active = models.BooleanField()
    ## timezone = timezone selector
    swag_options = [
        ('0', '0'),
        ('30', '30'),
        ('60', '60'),
        ('90', '90'),
        ('150', '150'),
        ('1000', '1000'),        
    ]
    swag_group = models.CharField(choices=swag_options, default='0')
    positions = Position()
    
    def __str__(self):
        return first_name + last_name