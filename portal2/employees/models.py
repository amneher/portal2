from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField('First Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=False, null=False)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    hire_date = models.DateField(auto_now=False, auto_now_add=False)
    date_left = models.DateField(auto_now=False, auto_now_add=False)
    status_choices = (
        (SALARY, 'Salary'),
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (TEMPORARY, 'Temporary'),
    )
    status = models.CharField(
        max_length=2,
        choices = status_choices,
        default = PART_TIME,
    )
    rfid = models.CharField(max_length=255, unique=True)
    hr_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    swag_group_choices = (
        (0, '0'),
        (30, '30'),
        (60, '60'),
        (90, '90'),
        (150, '150'),
        (1000, '1000'),
    )
    swag_group = models.CharField(max_length=4, choices=swag_group_choices, default=0)
    
