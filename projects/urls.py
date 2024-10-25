from rest_framework import routers
from django.urls import path, include
from projects.views.profile_view import ProfileViewSet
from projects.views.project_view import ProjectViewSet
from projects.views.certifying_institution_view import (
        CertificateViewSet,
        CertifyingInstitutionViewSet
    )



router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)

urlpatterns = [
    path("", include(router.urls))
]