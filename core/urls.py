from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, CourierViewSet, DeliveryOrderViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'couriers', CourierViewSet, basename='courier')
router.register(r'orders', DeliveryOrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
