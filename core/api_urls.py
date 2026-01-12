from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PassengerViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'passengers', PassengerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]

