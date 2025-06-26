from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

def criar_pedido_usuario(request):
    produtos = Product.objects.all()
    return render(request, 'compra_usuario/criar_pedido.html', {'produtos': produtos})

def home(request):
    return render(request, 'home/home.html')

def admin_custom(request):
    return render(request, 'admin_custom.html')