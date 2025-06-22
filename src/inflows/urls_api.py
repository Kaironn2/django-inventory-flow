from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.InflowCreateListView.as_view(),
         name='inflow-create-list-api-view'
    ),
    path(
        '<int:pk>/',
        views.InflowRetrieveUpdateDestroyView.as_view(),
        name='inflow-detail-api-view'
    )
]
