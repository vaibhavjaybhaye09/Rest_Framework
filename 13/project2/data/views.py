
from rest_framework import viewsets
from .models import Details
from .serializers import DetailsSerializer

# Create your views here.

class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all().order_by('-id')
    serializer_class = DetailsSerializer