from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ServerView, ServersView

urlpatterns = [
    path('', ServerView.as_view(), name='server'),
    path('<str:username>/', ServersView.as_view(), name='servers'),
]
