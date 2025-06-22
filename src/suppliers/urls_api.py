from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.SupplierCreateListView.as_view(),
         name='supplier-create-list-api-view'
    ),
    path(
        '<int:pk>/',
        views.SupplierRetrieveUpdateDestroyView.as_view(),
        name='supplier-detail-api-view'
    )
]
