from django.contrib import admin

from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'depot_lat',
                    'deopt_long',
                    'inspector_zone',
                    'starting_time',
                    'finishing_time',
                    'service_time',)

# Register your models here.
#User name is:  AhmedFathy
#Email is:  fakemail@gmail.com
#password is:  T@haluf2021
admin.site.register(Employee, EmployeeAdmin)
