from django.urls import path
from . import views

urlpatterns = [
    path('create-superuser/', views.create_superuser, name='create_superuser'),
]
