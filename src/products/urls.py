from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product-list'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]
