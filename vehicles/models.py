from django.db import models

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

    
    def __str__(self):
        return self.vehicle_number