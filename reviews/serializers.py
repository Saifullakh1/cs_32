from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewForClinicSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name')

    class Meta:
        model = Review
        fields = ['id', 'user_name', 'image', 'description', 'rating']
