from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()
router.register('car', CarViewSet ,basename='car')

urlpatterns = router.urls