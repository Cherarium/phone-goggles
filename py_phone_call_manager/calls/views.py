from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CallEventViewSet

router = DefaultRouter()
router.register(r'calls', CallEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
