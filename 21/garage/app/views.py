from rest_framework import viewsets
from .models import  Garage
from .serializers import GarageSerializers

class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all().order_by('-id')
    serializer_class = GarageSerializers
    