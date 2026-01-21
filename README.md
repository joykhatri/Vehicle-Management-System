# Vehicle-Management-System
It is Django &amp; Django rest framework based project. With CRUD APIs.

install django & django rest framework.
-> pip install django djangorestframework
-> django-admin startproject vehicle_system .
-> django-admin startapp vehicles

Add apps to INSTALLED_APPS in vehicle_system/settings.py:INSTALLED_APPS = [
    ...
    'rest_framework',
    'vehicles',
]

after creating model.py
python manage.py makemigrations
python manage.py migrate

Register the Vehicle model in vehicles/admin.py:

Create vehicles/serializers.py:
Create vehicles/views.py:
Create vehicles/urls.py:
Include app URLs in vehicle_system/urls.py:

for APIs testing - Postman

APIs endpoint:
1. /api/vehicles/(POST)
   for register vehicle
enter data in payload(JSON format):
{
  "vehicle_number": "",
  "owner_name": "",
  "vehicle_type": "",
  "registration_date": "",
  "is_active": 
}

2. /api/vehicles/(GET)
   to get vehicles data

3. to check vehicle type(GET)
   /api/vehicles/?vehicle_type=

4. Search Vehicles(GET)
   /api/vehicles/?search=

5. update data(PUT)
   /api/vehicles/{id}/

   enter data in payload for update
   {
  "vehicle_number": "",
  "owner_name": "",
  "vehicle_type": "",
  "registration_date": "",
  "is_active": 

  }

6. delete data(DELETE)
   /api/vehicles/{id}/

7. for register the user(POST)
   /api/register/

   enter the data in payload
   {
    "username": "",
    "email": "",
    "password": ""
  }

8. for login the user(POST)
   /api/login/

   enter the data in payload
   {
    "username": "", 
    "password": ""
  }
