from django.contrib import admin
from .models import Vehicle

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'password')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'owner_name', 'vehicle_type', 'registration_date', 'is_active')
