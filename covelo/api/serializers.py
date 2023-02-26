from .models import Locker
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Bicycle, Station, Locker

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    # Define fields for serialization/deserialization
    # Note: 'password' is write-only to prevent exposing user's password
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    type = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'name', 'age', 'type']

    def create(self, validated_data):
        # Create a new user with validated data
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class BicycleSerializer(serializers.ModelSerializer):
    locker = LockerSerializer()
    station = serializers.SerializerMethodField()

    class Meta:
        model = Bicycle
        fields = ['bicycle_id', 'is_good', 'locker', 'station']

    def get_station(self, obj):
        return obj.locker.station.location if obj.locker else None
