from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from home.views import admin_custom

urlpatterns = [
    path('admin-custom/', admin_custom, name='admin-custom'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('admin/logout/', auth_views.LogoutView.as_view(), name='logout'),
]