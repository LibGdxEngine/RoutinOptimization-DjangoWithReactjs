from django.shortcuts import render

from rest_framework import viewsets
from .serializers import EmployeeSerizalizer
from .models import Employee

# Create your views here.

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerizalizer
    queryset = Employee.objects.all()