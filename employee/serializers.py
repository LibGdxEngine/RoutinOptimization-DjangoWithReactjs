from rest_framework import serializers
from .models import Employee

class EmployeeSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name',
                  'depot_lat',
                  'deopt_long',
                  'inspector_zone',
                  'starting_time',
                  'finishing_time',
                  'service_time',
                  )