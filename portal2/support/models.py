import uuid
from django.db import models

# Create your models here.
class Ticket(models.model):

	def __str__(self):
		return self.name

	closed = "CL"
	open = "OP"
	waiting = "WT"
	in_progress = "IP"

	status_choices = [
		(closed, 'Closed'),
		(open, 'Open'),
		(waiting, 'Waiting'),
		(in_progress, 'In Progress'),
	]

	beer_lines = "BL"
	brewing_internal = "BR"
	it = "IT"
	custodial = "CS"
	equipment = "EQ"
	facilities = "FC"
	qa = "QA"
	safety = "SF"

	type_choices = [
		(beer_lines, 'Beer Lines'),
		(brewing_internal, 'Brewing'),
		(it, 'IT'),
		(custodial, 'Custodial'),
		(equipment, 'Equipment'),
		(facilities, 'Facilities'),
		(qa, 'Quality Assurance'),
		(safety, 'Safety'),
	]

	grove = "GR"
	midtown = "MT"
	urb = "UR"

	locations = [
		(grove, 'Grove'),
		(midtown, 'Midtown'),
		(urb, 'URB'),
	]

	low = "LO"
	medium = "MD"
	high = "HI"

	severity_levels = [
		(low, 'Low'),
		(medium, 'Medium'),
		(high, 'High'),
	]

	name = models.CharField(max_length=255)
	ticket_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_due = models.DateTimeField()
	status = models.CharField(max_length=2, choices = status_choices, default = open)
	description = models.TextField()
	comments = []
	location = models.CharField(max_length=2, choices = locations)
	type = models.CharField(max_length=2, choices = type_choices)
	severity = models.CharField(max_length=2, choices = severity_levels)


# what attributes does the ticket class need?
# name, date created, due date, current status, comments, location, type, assignees, ticket number, priority
