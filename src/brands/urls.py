from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.BrandListView.as_view(), name='brand-list'),
    path('create/', views.BrandCreateView.as_view(), name='brand-create'),
    path('<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand-update'),
    path('<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand-delete'),
]
