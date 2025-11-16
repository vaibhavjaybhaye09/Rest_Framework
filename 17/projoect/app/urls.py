from .views import ProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api', ProfileViewSet, basename='api')

urlpatterns = router.urls