from django import forms
from .models import Customer, Service, Staff, Appointment, Inventory

class CustomerForm(forms.ModelForm):
    class Meta: model = Customer; fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta: model = Service; fields = '__all__'

class StaffForm(forms.ModelForm):
    class Meta: model = Staff; fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta: model = Appointment; fields = '__all__'

class InventoryForm(forms.ModelForm):
    class Meta: model = Inventory; fields = '__all__'
#forms.py