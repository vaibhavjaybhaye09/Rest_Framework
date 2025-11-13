from rest_framework.routers import DefaultRouter
from .views import DetailsViewSet


router = DefaultRouter()
router.register('details', DetailsViewSet ,basename='details')

urlpatterns = router.urls