# core/forms.py
from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'passport_number', 'nationality', 'birth_date']
        
 
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }