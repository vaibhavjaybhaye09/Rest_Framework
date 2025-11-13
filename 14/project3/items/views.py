from rest_framework import viewsets
from .models import Items
from .serializers import ItemsSerializer


# Create your views here.
class ItemsViewsets(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('-id')
    serializer_class = ItemsSerializer
