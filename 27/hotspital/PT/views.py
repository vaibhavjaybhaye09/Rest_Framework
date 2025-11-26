from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSeralizer

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-id')
    serializer_class = PatientSeralizer

    
