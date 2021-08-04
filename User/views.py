from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile


# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': "Hello world. test"}
        return Response(content)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ProfileSerializer

    def get(self, request, username, *args, **kwargs):
        profile = Profile.objects.get(user=User.objects.get(username=username))
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def put(self, request, username, *args, **kwargs):
        profile = Profile.objects.get(user=User.objects.get(username=username))
        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
