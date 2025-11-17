from rest_framework.routers import DefaultRouter
from .views import TodoViewSet


router = DefaultRouter()
router.register('api', TodoViewSet ,basename='api')

urlpattern = router.urls