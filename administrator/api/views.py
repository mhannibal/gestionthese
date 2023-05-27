from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from administrator.models import Administrator, AdministratorProfile
from administrator.api.serializers import AdministratorProfileSerializer, AdministratorSerializer

class AdministratorViewSet(viewsets.ModelViewSet):

    serializer_class = AdministratorSerializer
    def get_queryset(self):
        return  Administrator.objects.filter()
    
class AdministratorProfileViewSet(viewsets.ModelViewSet):

    serializer_class = AdministratorProfileSerializer
    def get_queryset(self):
        return  AdministratorProfile.objects.filter()