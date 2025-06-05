from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # acessível em http://localhost:8000/
]