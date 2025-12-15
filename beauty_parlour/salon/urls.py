from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('customers/', views.customers, name='customers'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/edit/<int:id>/', views.customer_edit, name='customer_edit'),
    path('customers/delete/<int:id>/', views.customer_delete, name='customer_delete'),

    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add/', views.inventory_add, name='inventory_add'),

    path('billing/<int:appt_id>/', views.create_bill, name='create_bill'),
]