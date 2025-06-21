from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('inflows/', include('inflows.urls')),
    path('outflows/', include('outflows.urls')),
    path('products/', include('products.urls')),
    path('suppliers/', include('suppliers.urls')),
]
