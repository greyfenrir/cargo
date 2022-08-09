from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User

from . import serializers
from .models import Shipment


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ShipmentList(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ShipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer
