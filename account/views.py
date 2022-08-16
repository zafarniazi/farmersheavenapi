from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.serializers import UserRegistrationSerializer
from account.serializers import UserLoginSerializer
from account.serializers import profileSerializer
from django.contrib.auth import authenticate
from account.renderes import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializers = UserRegistrationSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
           User = serializers.save()
           token = get_tokens_for_user(User)
           return Response({"token": token, "msg": "Registration sucessfull"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request):
        serializers = UserLoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):

         email = request.data.get('email')
         password = request.data.get('password')
         user = authenticate(request, email=email, password=password)
        if user is not None:
         token = get_tokens_for_user(user)
         return Response({'token': token, 'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
         return Response({'message': 'UserName or password incorrect'}, status=status.HTTP_404_NOT_FOUND)


class profile_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = profileSerializer(user)
        return Response(serializer.data)
