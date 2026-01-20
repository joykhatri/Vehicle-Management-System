from rest_framework.viewsets import ModelViewSet
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework import filters

class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['vehicle_number']

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        vehicle_type = self.request.query_params.get('vehicle_type')

        if vehicle_type:
            queryset = queryset.filter(vehicle_type=vehicle_type)

        return queryset