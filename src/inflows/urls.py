from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.InflowListView.as_view(), name='inflow-list'),
    path('create/', views.InflowCreateView.as_view(), name='inflow-create'),
    path('<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow-detail'),
]
