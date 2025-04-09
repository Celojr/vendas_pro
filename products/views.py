from django.shortcuts import render
from .models import Product

def index(request):
  product_list = Product.objects.all()
  context = {"product_list": product_list}
  return render(request, "products/index.html", context)

def detail(request, product_id):
  product = Product.objects.get(id=product_id)
  context = {"product": product}
  return render(request, "products/detail.html", context)