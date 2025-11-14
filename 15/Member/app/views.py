from rest_framework import viewsets
from .serializers import MemberSerailizer
from .models import Member


# Create your views here.

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-id')
    serializer_class = MemberSerailizer