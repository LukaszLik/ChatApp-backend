from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from .models import Server, ServerList
from rest_framework.permissions import AllowAny
from .serializers import ServerSerializer, ServerListSerializer


# Create your views here.
class ServerView(generics.CreateAPIView):
    queryset = Server.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ServerSerializer

    def get(self, request, server_name, *args, **kwargs):
        server = Server.objects.get(server_name=server_name)
        serializer = ServerSerializer(server, many=True)
        return Response(serializer.data)


class ServersView(generics.CreateAPIView):
    queryset = ServerList.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ServerListSerializer

    # filter instead of get when looking for multiple matching records
    def get(self, request, username, *args, **kwargs):
        servers = ServerList.objects.filter(user_id=User.objects.get(username=username).id)
        serializer = ServerListSerializer(servers, many=True)
        return Response(serializer.data)


# class ServerList(generics.CreateAPIView):
#     queryset = Server.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = ServerSerializer
#
#     def get(self, request, *args, **kwargs):
#         s_list = ServerList.objects.get()
#         serializer = ServerListSerializer(s_list, many=True)
#         return Response(serializer.data)
