from rest_framework import routers
from .views import VehicleViewSet, RegisterView, LoginView, ServiceHistoryViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.SimpleRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'service-history', ServiceHistoryViewSet, basename='service-history')
urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]