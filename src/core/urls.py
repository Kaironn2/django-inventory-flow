from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path


class HomeView(TemplateView):
    template_name = 'core/base.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
]
