from rest_framework import serializers
from .models import *
from account.models import User


class HealthAnalysisSerializer(serializers.ModelSerializer):
    """
    HealthAnalysis serializer
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = HealthAnalysis
        fields = ('id', 'name', 'bbox', 'coordinates', 'path', 'user')
