from rest_framework import serializers
from .models import Vehicle, ServiceHistory
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("already_registered")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("already_registered")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password']
    #     )
    #     return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class VehicleSerializer(serializers.ModelSerializer):
    assigned_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Vehicle
        fields = '__all__'

class ServiceHistorySerializer(serializers.ModelSerializer):
    # username = serializers.CharField(write_only=True)
    vehicle_number = serializers.CharField(write_only=True)
    vehicle = serializers.CharField(source='vehicle_number.vehicle_number', read_only=True)

    class Meta:
        model = ServiceHistory
        fields = [
            'id',
            'vehicle_number',
            'vehicle',
            'service_date',
            'service_type',
            'service_cost',
            'remarks',
        ]
    
    def create(self, validated_data):
        vehicle_number_str = validated_data.pop('vehicle_number')

        try:
            vehicle = Vehicle.objects.get(vehicle_number=vehicle_number_str)
        except Vehicle.DoesNotExist:
            raise serializers.ValidationError(
                {"vehicle_number": "Vehicle not found"}
            )

        return ServiceHistory.objects.create(
            vehicle_number=vehicle,
            **validated_data
        )