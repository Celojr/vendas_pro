from django.shortcuts import render
from .models import Order

def index(request):
  order_list = Order.objects.all()
  context = {"order_list": order_list}
  return render(request, "orders/index.html", context)

def detail(request, order_id):
  order = Order.objects.get(id=order_id)
  context = {"order": order}
  return render(request, "orders/detail.html", context)