from rest_framework import generics

from .serializers import ProjectSerializer
from projects.models import Project

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer