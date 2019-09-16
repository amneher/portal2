from django.db import models

from . import Project
from . import Employee

# Create your models here.
class Ticket (models.Model):
	create_date = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField()
	priority_options = [
		('1', 'Emergency'),
		('2', 'High'),
		('3', 'Medium'),
		('4', 'Low'),
		('5', 'Feature Improvement'),
	]
	priority = models.CharField(max_length=1, choices=priority_options, default='3')
	title = models.TextArea()
	description = models.TextArea()
	assignees = Employee()
	location_choices = [
		('GBB', 'Grove Brewery and Bierhall'),
		('MBB', 'Midtown Brewery and Biergarten'),
		('URB', 'Urban Research Brewery'),
	]
	location = models.CharField(max_length=3, choices=location_choices, default='GBB')
	status_choices = [
		('OP', 'Open'),
		('WT', 'Waiting'),
		('PP', 'Postponed'),
		('SC', 'Scheduled'),
		('IP', 'In Progress'),
		('CL', 'Closed'),
	]
	status = models.CharField(max_length=2, choices=status_choices, default='OP')
	repeat = models.Boolean()
	repeat_interval = models.DateTimeField()
	visibility = models.Boolean()
	project = Project()
	creator = Employee()

	def __str__(self):
	    return self.title

	def __unicode__(self):
		return self.title