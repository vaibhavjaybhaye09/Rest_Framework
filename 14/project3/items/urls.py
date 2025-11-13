from rest_framework.routers import DefaultRouter
from .views import ItemsViewsets


router = DefaultRouter()
router.register('item', ItemsViewsets, basename='item')

urlpatterns = router.urls