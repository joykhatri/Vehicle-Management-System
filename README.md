# 🚗 Vehicle Management System
A **Django & Django REST Framework** based Vehicle Management System that provides full CRUD APIs along with user authentication and vehicle assignment features.

## 📌 Features
- User Registration & Login
- Create, Read, Update, Delete Vehicles
- Search Vehicles
- Filter by Vehicle Type
- Assign Vehicle to User
- RESTful APIs

## 🛠️ Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (Default DB)

## ⚙️ Installation & Setup
### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
```

### 2️⃣ Activate Virtual Environment
```bash
Windows:
.venv\Scripts\activate

Mac/Linux:
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install django djangorestframework
```

### 4️⃣ Create Project & App
```bash
django-admin startproject vehicle_system .
django-admin startapp vehicles
```

### 5️⃣ Add Apps to INSTALLED_APPS
```bash
In vehicle_system/settings.py:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'vehicles',
]
```

### 🗄️ Database Setup
```bash
After creating models in models.py:

python manage.py makemigrations
python manage.py migrate
```

### ▶️ Run Development Server
```bash
python manage.py runserver
```

### Server will start at:
```bash
http://127.0.0.1:8000/
```

### 📁 Project Structure
```bash
vehicle_system/
│
├── vehicle_system/
│   ├── settings.py
│   ├── urls.py
│
├── vehicles/
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
└── manage.py
```

### 🔌 API Endpoints
```bash
Base URL:
http://127.0.0.1:8000/api/
```

### 1️⃣ Register Vehicle (POST)
#### Endpoint:
```bash
/api/vehicles/
```

#### Payload:
```bash
{
  "vehicle_number": "AB123CD",
  "owner_name": "John Doe",
  "vehicle_type": "Car",
  "registration_date": "2024-01-01",
  "is_active": true
}
```

### 2️⃣ Get All Vehicles (GET)
```bash
/api/vehicles/
```

### 3️⃣ Filter by Vehicle Type (GET)
```bash
/api/vehicles/?vehicle_type=Car
```

### 4️⃣ Search Vehicles (GET)
```bash
/api/vehicles/?search=John
```

### 5️⃣ Update Vehicle (PUT)
```bash
/api/vehicles/{id}/
```
#### Payload:
```bash
{
  "vehicle_number": "",
  "owner_name": "",
  "vehicle_type": "",
  "registration_date": "",
  "is_active": 
}
```

### 6️⃣ Delete Vehicle (DELETE)
```bash
/api/vehicles/{id}/
```

### 7️⃣ Register User (POST)
```bash
/api/register/
```
#### Payload:
```bash
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

### 8️⃣ Login User (POST)
```bash
/api/login/
```
#### Payload:
```bash
{
  "username": "john",
  "password": "password123"
}
```

### 9️⃣ Assign Vehicle to User (POST)
```bash
/api/vehicles/
```
#### Payload:
```bash
{
  "vehicle_number": "AB123CD",
  "owner_name": "John Doe",
  "vehicle_type": "Car",
  "registration_date": "2024-01-01",
  "is_active": true
}
```
#### Response:
```bash
{
  "status": true,
  "message": "Vehicle assigned successfully",
  "data": {
    "id": 1,
    "assigned_user": "john",
    "vehicle_number": "AB123CD",
    "owner_name": "John Doe",
    "vehicle_type": "Car",
    "registration_date": "2024-01-01",
    "is_active": true
  }
}
```

### 🧪 API Testing
#### You can test APIs using:
- Postman
- Thunder Client (VS Code Extension)
- cURL

### 👨‍💻 Admin Panel
#### To access Django Admin:

#### Create superuser:
```bash
python manage.py createsuperuser
```

#### Open:
```bash
http://127.0.0.1:8000/admin/
```

### 📌 Notes
- Make sure migrations are applied before running the server.
- Use virtual environment to avoid dependency conflicts.
- Configure authentication permissions if required.
