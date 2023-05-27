
from files.models import File
from .serializers import FileSerializer
from rest_framework import viewsets

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer