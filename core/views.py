from django.shortcuts import render, get_object_or_404, redirect
from .models import DeliveryOrder
from .forms import DeliveryOrderForm
from django.shortcuts import redirect
from .NetworkHelper import HotelAPI

def external_guests(request):
    guests = HotelAPI.get_guests()
    return render(request, "core/external_guests.html", {"guests": guests})



def order_list(request):
    orders = DeliveryOrder.objects.all()
    return render(request, 'core/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(DeliveryOrder, pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'core/order_detail.html', {'order': order})


def order_create(request):
    form = DeliveryOrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'core/order_form.html', {'form': form})


def order_update(request, pk):
    order = get_object_or_404(DeliveryOrder, pk=pk)
    form = DeliveryOrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_detail', pk=pk)
    return render(request, 'core/order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(DeliveryOrder, pk=pk)
    form = DeliveryOrderForm(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        return redirect('order_detail', pk=order.pk)

    return render(request, 'core/order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(DeliveryOrder, pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'core/order_confirm_delete.html', {'order': order})

from django.shortcuts import render

def external_guests(request):
    guests = []  
    return render(request, "core/external_guests.html", {
        "guests": guests
    })

import requests

API_BASE_URL = "http://127.0.0.1:8001/api"

class NetworkHelper:

    @staticmethod
    def get_guests():
        response = requests.get(f"{API_BASE_URL}/guests/")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_guest(guest_id):
        response = requests.delete(f"{API_BASE_URL}/guests/{guest_id}/")
        response.raise_for_status()
        return True


from django.shortcuts import redirect
from .NetworkHelper import HotelAPI


def delete_external_guest(request, guest_id):
    if request.method == "POST":
        HotelAPI.delete_guest(guest_id)
    return redirect("external_guests")
