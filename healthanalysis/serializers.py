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
                  'min_value', 'max_value', 'mean_value', 'area', 'user')


class YieldPredictionSerializer(serializers.Serializer):
    wheat_area = serializers.FloatField()
    nov16 = serializers.FloatField()
    dec2 = serializers.FloatField()
    dec18 = serializers.FloatField()
    feb18 = serializers.FloatField()
    march5 = serializers.FloatField()
    march21 = serializers.FloatField()
    april6 = serializers.FloatField()
    april22 = serializers.FloatField()
