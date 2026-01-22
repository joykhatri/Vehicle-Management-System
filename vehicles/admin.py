from django.contrib import admin
from .models import Vehicle, ServiceHistory

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'password')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'owner_name', 'vehicle_type', 'registration_date', 'is_active')

@admin.register(ServiceHistory)
class ServiceHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle_number', 'service_date', 'service_type', 'service_cost', 'remarks')