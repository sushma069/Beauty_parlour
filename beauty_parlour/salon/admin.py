#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Service, Staff, Appointment, Inventory, Bill

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Staff)
admin.site.register(Appointment)
admin.site.register(Inventory)
admin.site.register(Bill)
