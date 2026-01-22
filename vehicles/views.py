from rest_framework.viewsets import ModelViewSet
from .models import Vehicle, ServiceHistory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import VehicleSerializer, RegisterSerializer, LoginSerializer, ServiceHistorySerializer
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.db import IntegrityError

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": True,
                "message": "User created successfully",
                "data": {"username": user.username,
                        "email": user.email,
                        "password": user.password}
                }, status=status.HTTP_201_CREATED)
        
        errors = serializer.errors
        if 'username' in errors and 'required' in str(errors['username'][0]).lower():
            message = "Username is required."
        elif 'password' in errors and 'required' in str(errors['password'][0]).lower():
            message = "Password is required."
        else:
            is_duplicate = False
            for field in ['username', 'email']:
                if field in errors:
                    if any(str(e) == "already_registered" for e in errors[field]):
                        is_duplicate = True
                        break

            if is_duplicate:
                message = "Username or email already registered"
            else:
                message = "Invalid username or email"

        return Response({
            "status": False,
            "message": message,
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)
        

    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            if not username:
                return Response({
                    "status": False,
                    "message": "Username is required.",
                    "data": None
                }, status=status.HTTP_400_BAD_REQUEST)

            if not password:
                return Response({
                    "status": False,
                    "message": "Password is required.",
                    "data": None
                }, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(username=username, password=password)
            if user is None:
                return Response({
                    "status": False,
                    "message": "Invalid credentials",
                    "data": None
                }, status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)

            return Response({
                "status": True,
                "message": "Login successful",
                "data": {
                    "username": user.username,
                    "email": user.email
                },
                "tokens": {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }
            }, status=status.HTTP_200_OK)

        error_messages = []
        for field, errors in serializer.errors.items():
            for error in errors:
                error_messages.append(f"{field.capitalize()} is required." if "required" in str(error).lower() else str(error))

        return Response({
            "status": False,
            "message": " ".join(error_messages),
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)

    

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
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "status": True,
                "message": "Vehicle successfully registered",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
        error_messages = []
        for field, errors in serializer.errors.items():
            for error in errors:
                error_messages.append(f"{field.replace('_', ' ').capitalize()}: {str(error)}")

        return Response({
            "status": False,
            "message": " ".join(error_messages),
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)




class ServiceHistoryViewSet(ModelViewSet):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer

    def get_queryset(self):
        queryset = ServiceHistory.objects.all()

        vehicle_id = self.request.query_params.get('vehicle')
        if vehicle_id:
            queryset = queryset.filter(vehicle_id=vehicle_id)
        return queryset

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = serializer.save()
        
        return Response({
            "status": True,
            "message": "Service history added successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)