from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.ProductCreateListView.as_view(),
         name='product-create-list-api-view'
    ),
    path(
        '<int:pk>/',
        views.ProductRetrieveUpdateDestroyView.as_view(),
        name='product-detail-api-view'
    )
]
