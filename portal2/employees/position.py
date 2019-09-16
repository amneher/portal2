from django.db import models

class Position(models.Model):
    name = models.CharField()
    department_choices = [
        ('BR', 'Brewery'),
        ('CF', 'Co-Founders'),
        ('EV', 'Events'),
        ('FI', 'Finance'),
        ('GB', 'German Brewery'),
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('KT', 'Kitchen'),
        ('MT', 'Maintenance'),
        ('MK', 'Marketing'),
        ('OP', 'Operations'),
        ('PK', 'Packaging'),
        ('QA', 'Quality Assurance'),
        ('RT', 'Retail'),
        ('SL', 'Sales'),
        ('TR', 'Taste Room'),
    ]
    department = models.CharField(max_length=2, choices=department_choices)
    is_active = models.BooleanField()