from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from group.models import Group, Subject
from group.api.serializers import GroupSerializer, SubjectSerializer

class GroupViewSet(viewsets.ModelViewSet):

    serializer_class = GroupSerializer
    def get_queryset(self):
        return  Group.objects.filter()
    
class SubjectViewSet(viewsets.ModelViewSet):

    serializer_class = SubjectSerializer
    def get_queryset(self):
        return  Subject.objects.filter()
    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)