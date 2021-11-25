from django.db import models

class Trip(models.Model):
    High = 'High'
    Normal = 'Normal'
    Low = 'Low'
    PRIORITIES = [
        (High, 'High'),
        (Normal, 'Normal'),
        (Low, 'Low'),
    ]
    name = models.CharField(max_length=120)
    destination_lat = models.DecimalField(max_digits=15, decimal_places=9)
    destination_long = models.DecimalField(max_digits=15, decimal_places=9)
    priority = models.CharField(max_length=6, choices=PRIORITIES, default=Normal)
    visiting_date = models.DateField(null=True)

    def _str_(self):
        return self.name
