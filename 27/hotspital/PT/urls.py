from rest_framework.routers import  DefaultRouter
from .views import  PatientViewSet

router = DefaultRouter()
router.register('pt', PatientViewSet ,'pt')

urlpatterns = router.urls