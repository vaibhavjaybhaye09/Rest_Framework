from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()
router.register('api', CourseViewSet,basename='api')

urlpattern = router.urls