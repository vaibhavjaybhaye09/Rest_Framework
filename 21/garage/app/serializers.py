from rest_framework import serializers
from .models import Garage

class GarageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'