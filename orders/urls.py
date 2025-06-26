from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:order_id>/", views.detail, name="detail"),
    path('', views.index, name='orders'),
    path('criar-pedido/', views.criar_pedido_usuario, name='criar_pedido'),
]