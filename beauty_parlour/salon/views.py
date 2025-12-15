#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Customer, Service, Staff, Appointment, Inventory, Bill
from .forms import CustomerForm, ServiceForm, StaffForm, AppointmentForm, InventoryForm

def dashboard(request):
    return render(request, "salon/dashboard.html", {
        "customers": Customer.objects.count(),
        "services": Service.objects.count(),
        "appointments": Appointment.objects.count()
    })

def customers(request):
    q = request.GET.get("q")
    customers = Customer.objects.filter(name__icontains=q) if q else Customer.objects.all()
    return render(request, "salon/customers.html", {"customers": customers, "query": q})

def customer_add(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect("customers")
    return render(request, "salon/form.html", {"form": form, "title": "Add Customer"})

def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid(): form.save(); return redirect("customers")
    return render(request, "salon/form.html", {"form": form, "title": "Edit Customer"})

def customer_delete(request, id):
    get_object_or_404(Customer, id=id).delete()
    return redirect("customers")

def inventory(request):
    q = request.GET.get("q")
    items = Inventory.objects.filter(item_name__icontains=q) if q else Inventory.objects.all()
    return render(request, "salon/inventory.html", {"items": items, "query": q})

def inventory_add(request):
    form = InventoryForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect("inventory")
    return render(request, "salon/form.html", {"form": form, "title": "Add Inventory Item"})

def create_bill(request, appt_id):
    appt = Appointment.objects.get(id=appt_id)
    bill = Bill.objects.create(
        appointment=appt,
        total_amount=appt.service.price
    )
    return render(request, "salon/bill.html", {"bill": bill})
