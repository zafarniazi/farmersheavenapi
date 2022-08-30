from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from account.views import UserRegistrationView
from account.views import LoginView
from account.views import profile_view
from account.views import UserChangePasswordView

urlpatterns = [

    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', profile_view.as_view(), name='profile'),
    path('change_password', UserChangePasswordView.as_view(), name='change')

]
