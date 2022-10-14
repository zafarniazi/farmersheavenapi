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
        fields = ('id', 'name', 'bbox', 'coordinates', 'path', 'time_from', 'time_to',
                  'min_value', 'max_value', 'mean_value', 'yield_area', 'user')


class YieldPredictionSerializer(serializers.Serializer):
    rain = serializers.FloatField()
    rel_hum = serializers.FloatField()
    cloud = serializers.FloatField()
    avg_sun = serializers.FloatField()
    temp = serializers.FloatField()
    ndvi = serializers.FloatField()
    hectares = serializers.FloatField()
