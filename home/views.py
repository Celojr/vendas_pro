from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def admin_custom(request):
    return render(request, 'admin_custom.html')