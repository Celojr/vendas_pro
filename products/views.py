from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the products index.")

def detail(request, product_id):
  return HttpResponse("Hello, world. You're at the product dtail.")