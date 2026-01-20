from rest_framework import routers
from .views import VehicleViewSet

router = routers.SimpleRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
urlpatterns = router.urls