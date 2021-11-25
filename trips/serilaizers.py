from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'destination_lat', 'destination_long',
                  'priority',
                  'visiting_date',
                  )