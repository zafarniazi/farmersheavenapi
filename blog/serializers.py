from rest_framework import serializers
from .models import *
from account.models import User
from blog.models import blog


class BlogSerializer(serializers.ModelSerializer):
    """
    Blog serializer
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = blog
        fields = '__all__'
