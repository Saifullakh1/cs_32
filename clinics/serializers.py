from rest_framework import serializers
from .models import Clinic
from reviews.serializers import ReviewForClinicSerializer


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = '__all__'


class ClinicRetrieveSerializer(serializers.ModelSerializer):
    clinic_reviews = ReviewForClinicSerializer(many=True)

    class Meta:
        model = Clinic
        fields = ['id', 'title', 'description', 'address', 'phone', 'image', 'clinic_reviews']