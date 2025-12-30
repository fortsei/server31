from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/edit/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path("external/guests/", views.external_guests, name="external_guests"),
    path("external/guests/<int:guest_id>/delete/", views.delete_external_guest, name="delete_external_guest"),
    path('dashboard/', views.dashboard_v1, name='dashboard'),
    path('dashboard/v2/', views.dashboard_v2, name='dashboard_v2'), 
    path('api/analytics/', views.AnalyticsAPIView.as_view(), name='analytics_api'),
]