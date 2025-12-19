from django import forms
from .models import DeliveryOrder

class DeliveryOrderForm(forms.ModelForm):
    class Meta:
        model = DeliveryOrder
        fields = ['customer', 'courier', 'address', 'price']
