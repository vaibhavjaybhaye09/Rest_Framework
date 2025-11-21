from rest_framework.routers import DefaultRouter
from .views import GarageViewSet

router = DefaultRouter()
router.register('garage', GarageViewSet ,'garage')

urlpatterns = router.urls
