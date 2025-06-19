from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),

    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('inflows/', include('inflows.urls')),
    path('suppliers/', include('suppliers.urls')),
]
