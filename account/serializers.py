from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validators_password(self, attr):
        password = attr.get('password')
        password2 = attr.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords must match")

        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = User
        fields = ('email', 'password')


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name')


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
          raise serializers.ValidationError(
              'password and password2 must be the same')
        user.set_password(password)
        user.save()
        return attrs
