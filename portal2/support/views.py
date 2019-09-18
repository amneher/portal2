from rest_framework import viewsets

from django.contrib.auth.models import Ticket, Project
from . import TicketSerializer
from . import ProjectSerializer
# Create your views here.


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer