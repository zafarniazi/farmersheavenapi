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
    Area = serializers.FloatField()
    Nitrogen = serializers.IntegerField()
    Phosphorus = serializers.IntegerField()
    Pottasium = serializers.IntegerField()
    pH = serializers.IntegerField()
    NDVI = serializers.FloatField()
    maxtemp = serializers.FloatField()
    relativehumidity = serializers.FloatField()
    dewpoints = serializers.FloatField()
    minwindspeed = serializers.FloatField()
    maxwindspeed = serializers.FloatField()
    cloudcoverage = serializers.FloatField()
