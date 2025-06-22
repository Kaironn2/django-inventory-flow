from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.OutflowCreateListView.as_view(),
         name='outflow-create-list-api-view'
    ),
    path(
        '<int:pk>/',
        views.OutflowRetrieveUpdateDestroyView.as_view(),
        name='outflow-detail-api-view'
    )
]
