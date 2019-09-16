from django.db import models
from . import Employee
from . import Ticket


class Project(models.Model):
    
    name = models.TextField()
    description = models.TextArea()
    visibility = models.Boolean()
    assignees = Employee()
    related_tickets = Ticket()
    

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
    
    
