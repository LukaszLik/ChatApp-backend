from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from User import views

urlpatterns = [
    path('login/', obtain_auth_token, name='api-token-auth'),
    path('register/', views.RegisterView.as_view(), name='auth-register'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name='profile-view'),
]