from rest_framework import viewsets
from projects.models import Profile
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from projects.serializers.profile_serializer import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def retrieve(self, request, *args, **kwargs):
        if request.method == 'GET':
            id = kwargs.get('pk')
            profile = get_object_or_404(self.queryset, id=id)
            context = {
                'profile': profile,
                'projects': profile.projects.all(),
                'certificates': profile.certificates.all()
            }
            print(profile.certificates.all())
            return render(request, "profile_detail.html", context)
        return super().retrieve(request, *args, **kwargs)