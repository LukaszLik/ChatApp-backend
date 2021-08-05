from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Server, ServerList


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"


class ServerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerList
        fields = "__all__"

