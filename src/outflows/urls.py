from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.OutflowListView.as_view(), name='outflow-list'),
    path('create/', views.OutflowCreateView.as_view(), name='outflow-create'),
    path('<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow-detail'),
]
