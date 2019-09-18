from rest_framework import serializers

from . import Employee, Position


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['name', 'department', 'is_active']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'birthdate', 'hire_date',
                  'left_date', 'status', 'rfid', 'hrid', 'is_employed', 'is_active', 'swag_group', 'positions', ]
