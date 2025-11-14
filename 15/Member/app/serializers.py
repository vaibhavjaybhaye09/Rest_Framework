from rest_framework import serializers
from .models import Member

class MemberSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'