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
    SALARY = 'SA'
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    TEMPORARY = 'TM'
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
    position = models.ForeignKey('Position', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name



class Position(models.Model):
    name = models.CharField('Position', max_length=255, blank=False, null=False, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField('Department', max_length=255, blank=False, null=False, unique=True)
    supervisor = models.ForeignKey('Employee', on_delete=models.CASCADE)
    admin = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='+', default=0)
    purchase_threshold = models.CharField(max_length=10, default='$0')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
