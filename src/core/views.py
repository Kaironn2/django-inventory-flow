import json

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from .metrics import Metrics


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):  # noqa: PLR6301
        context = super().get_context_data(**kwargs)
        context['products_metrics'] = Metrics.get_products_metrics()
        context['sales_metrics'] = Metrics.get_sales_metrics()
        context['daily_sales_data'] = json.dumps(Metrics.get_daily_sales_data())
        context['daily_sales_quantity_data'] = json.dumps(
            Metrics.get_daily_sales_quantity_data()
        )
        context['product_by_brand_data'] = json.dumps(
            Metrics.get_product_by_brand_data()
        )
        context['product_by_category_data'] = json.dumps(
            Metrics.get_product_by_category_data()
        )
        return context


class CustomLoginView(LoginView):
    template_name = 'core/login.html'


class CustomLogoutView(LogoutView):
    next_page = 'login'
