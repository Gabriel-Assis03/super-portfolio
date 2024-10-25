from rest_framework import viewsets
from projects.models import Certificate, CertifyingInstitution
from projects.serializers.certifying_institution_serializer import (
    CertificateSerializer,
    CertifyingInstitutionSerializer
    )


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer