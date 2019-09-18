from django.contrib.auth.models import Employee, Position
from rest_framework import viewsets

from portal2.employees.serializers import EmployeeSerializer, PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
