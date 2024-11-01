from rest_framework import viewsets
from projects.models import Project
from projects.serializers.project_serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer