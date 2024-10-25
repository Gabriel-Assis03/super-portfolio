from rest_framework import serializers
from projects.models import Certificate, CertifyingInstitution

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['name']


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = '__all__'

    def create(self, validated_data):
        certificates_data = validated_data.pop('certificates')
        certifying_institution_data = CertifyingInstitution.objects.create(**validated_data)
        for certificate in certificates_data:
            certificate = Certificate.objects.create(
                certifying_institution=certifying_institution_data, **certificate
            )
        return certifying_institution_data