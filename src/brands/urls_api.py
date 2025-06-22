from django.urls import path

from . import views

urlpatterns = [
    path('', views.BrandCreateListView.as_view(), name='brand-create-list-api-view'),
    path(
        '<int:pk>/',
        views.BrandRetrieveUpdateDestroyView.as_view(),
        name='brand-detail-api-view'
    )
]
