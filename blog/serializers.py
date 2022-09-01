from rest_framework import serializers
from .models import *
from account.models import User
from account.serializers import profileSerializer
from blog.models import blog


class BlogSerializer(serializers.ModelSerializer):
    """
    Blog serializer
    """
    # user = serializers.SlugRelatedField(
    #     slug_field="name", queryset=User.objects.all())
    user = profileSerializer()


    class Meta:
        model = blog
        fields = '__all__'
