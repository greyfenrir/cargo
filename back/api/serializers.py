from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shipment
        fields = ['id', 'created', 'from_addr', 'to_addr', 'state', 'owner']


class UserSerializer(serializers.ModelSerializer):
    shipments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'shipments']
