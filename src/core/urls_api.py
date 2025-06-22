from django.urls import include, path

urlpatterns = [
    path('authentication/', include('authentication.urls_api')),
    path('brands/', include('brands.urls_api')),
    path('categories/', include('categories.urls_api')),
    path('inflows/', include('inflows.urls_api')),
    path('outflows/', include('outflows.urls_api')),
    path('products/', include('products.urls_api')),
    path('suppliers/', include('suppliers.urls_api')),
]
