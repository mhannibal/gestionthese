from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from supervisor.models import Supervisor, SupervisorProfile
from supervisor.api.serializers import SupervisorProfileSerializer, SupervisorSerializer

class SupervisorViewSet(viewsets.ModelViewSet):

    serializer_class = SupervisorSerializer
    def get_queryset(self):
        return  Supervisor.objects.filter()
    
class SupervisorProfileViewSet(viewsets.ModelViewSet):

    serializer_class = SupervisorProfileSerializer
    def get_queryset(self):
        return  SupervisorProfile.objects.filter()