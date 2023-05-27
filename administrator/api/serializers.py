from rest_framework import serializers
from administrator.models import AdministratorProfile, Administrator

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'

class AdministratorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministratorProfile
        fields = ['description']