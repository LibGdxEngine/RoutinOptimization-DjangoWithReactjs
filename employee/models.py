from django.db import models

from django.db import models

# Create your models here.

class Employee(models.Model):
    AbuDhabi = 'Abu Dhabi'
    AlAin = 'Al Ain'
    Dubai = 'Dubai'
    Sharjah = 'Sharjah'
    Ajman = 'Ajman'
    EMIRATES_CHOICES = [
        (AbuDhabi, 'Abu Dhabi'),
        (AlAin, 'Al Ain'),
        (Dubai, 'Dubai'),
        (Sharjah, 'Sharjah'),
        (Ajman, 'Ajman'),
    ]
    name = models.CharField(max_length=120)
    depot_lat = models.DecimalField(max_digits=15, decimal_places=9)
    deopt_long = models.DecimalField(max_digits=15, decimal_places=9)
    inspector_zone = models.CharField(max_length=10, choices=EMIRATES_CHOICES, default=AbuDhabi)
    starting_time = models.TimeField(blank=True)
    finishing_time = models.TimeField(blank=True)
    service_time = models.IntegerField(blank=True)

    def _str_(self):
        return self.name
