from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
]