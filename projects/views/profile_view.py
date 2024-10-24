from rest_framework import viewsets
from ..models import Profile
from ..serializers.profile_serializer import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer