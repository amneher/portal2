from rest_framework import serializers
from employees.models import Employee, Position, Department

class EmployeeSerializer(serializers.Serializer):

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'birthday',
            'hire_date',
            'date_left',
            'status',
            'rfid',
            'hr_id',
            'is_active',
            'swag_group',
            'position',
        )

class PositionSerializer(serializers.Serializer):

    class Meta:
        model = Position
        fields = (
            'name',
            'department',
            'is_active',
        )

class DepartmentSerializer(serializers.Serializer):

    class Meta:
        model = Department
        fields = (
            'name',
            'supervisor',
            'admin',
            'purchase_threshold',
            'is_active',
        )
