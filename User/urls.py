from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from User import views

urlpatterns = [
    path('user/login/', obtain_auth_token, name='api-token-auth'),
    path('user/register/', views.RegisterView.as_view(), name='auth-register'),
]