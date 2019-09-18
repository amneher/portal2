from django.contrib.auth.models import Employee, Project, Ticket, Position
from rest_framework import serializers


# Serializers define the API representation.
#class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
  #      model = Employee
   #     fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'birthdate', 'hire_date',
    #              'left_date', 'status', 'rfid', 'hrid', 'is_employed', 'is_active', 'swag_group', 'positions', ]
        
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'visibility', 'assignees', 'related_tickets']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['create_date', 'due_date', 'priority', 'title', 'description', 'assignees', 'location', 'status', 'repeat', 'repeat_interval', 'visibility', 'project', 'creator',]
        

#class PositionSerializer(serializers.HyperlinkedModelSerializer):
 #   class Meta:
  #      model = Position
   #     fields = ['name', 'department', 'is_active']