from rest_framework.viewsets import ModelViewSet
from .models import Vehicle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import VehicleSerializer, RegisterSerializer, LoginSerializer
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "success": True,
                "message": "User created successfully",
                "data": {"username": user.username,
                         "email": user.email,
                         "password": user.password}
                }, status=status.HTTP_201_CREATED)

        if "email" in serializer.errors or "username" in serializer.errors:
            return Response({
                "success": False,
                "message": "User already registerd",
                "data": serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            
            if user is None:
                return Response(
                    {"success": False,
                    "message": "Invalid credentials",
                    "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            refresh = RefreshToken.for_user(user)
            return Response({
                "success": True,
                "message": "Login Successful",
                "data":{"username": user.username,
                        "password": user.password},
                "tokens":{        
                "access": str(refresh.access_token),
                "refresh": str(refresh)},
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['vehicle_number']

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        vehicle_type = self.request.query_params.get('vehicle_type')

        if vehicle_type:
            queryset = queryset.filter(vehicle_type=vehicle_type)

        return queryset

    def perform_create(self, serializer):
        serializer.save(assigned_user=self.request.user)