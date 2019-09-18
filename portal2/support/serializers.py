from django.contrib.auth.models import Project, Ticket
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'visibility',
                  'assignees', 'related_tickets']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['create_date', 'due_date', 'priority', 'title', 'description', 'assignees',
                  'location', 'status', 'repeat', 'repeat_interval', 'visibility', 'project', 'creator', ]
