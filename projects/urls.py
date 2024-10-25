from rest_framework import routers
from django.urls import path, include
from projects.views.profile_view import ProfileViewSet
from projects.views.project_view import ProjectViewSet



router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path("", include(router.urls))
]