from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ServerView, ServersView

urlpatterns = [
    path('', ServersView.as_view(), name='servers'),
]
