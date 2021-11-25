from django.contrib import admin

from django.contrib import admin
from .models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination_lat',
                    'destination_long',
                    'priority',
                    'visiting_date',
                    )


# Register your models here.
# User name is:  AhmedFathy
# Email is:  fakemail@gmail.com
# password is:  T@haluf2021
admin.site.register(Trip, TripAdmin)
