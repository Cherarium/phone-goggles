from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CallEventViewSet

router = DefaultRouter()

# Register the CallEventViewSet with the router
router.register(r'calls', CallEventViewSet)

# Defines the urlpatterns for the API endpoints
urlpatterns = [
    path('', include(router.urls)),
]
