from django.contrib import admin
from .models import Customer, Courier, DeliveryOrder

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone')

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vehicle')

@admin.register(DeliveryOrder)
class DeliveryOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'courier', 'price', 'created_at')
    list_filter = ('courier', 'customer')