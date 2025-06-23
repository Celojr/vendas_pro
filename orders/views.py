from django.shortcuts import render
from .models import Order

def index(request):
  orders = Order.objects.all()
  context = {"orders": orders}
  return render(request, "orders/index.html", context)

def detail(request, order_id):
  order = Order.objects.get(id=order_id)
  context = {"order": order}
  return render(request, "orders/detail.html", context)