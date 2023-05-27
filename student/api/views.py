from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student, StudentProfile
from student.api.serializers import StudentProfileSerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = StudentSerializer
    def get_queryset(self):
        return  Student.objects.filter()
    
class StudentProfileViewSet(viewsets.ModelViewSet):

    serializer_class = StudentProfileSerializer
    def get_queryset(self):
        return  StudentProfile.objects.filter()