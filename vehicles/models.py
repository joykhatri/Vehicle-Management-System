from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     username = models.CharField(max_length=15)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=500)

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=12, unique=True)
    owner_name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=10, choices=[
        ('CAR', 'Car'),
        ('BIKE', 'Bike'),
        ('TRUCK', 'Truck'),
    ])
    registration_date = models.DateField()
    is_active = models.BooleanField(default=True)
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicles')

    
    def __str__(self):
        return self.vehicle_number