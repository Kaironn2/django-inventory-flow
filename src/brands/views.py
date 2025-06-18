from django.shortcuts import render
from django.views.generic import ListView

from . import models


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brands/brand-list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(self.request, 'brands/partials/_brand_table.html', context)
        return super().render_to_response(context, **response_kwargs)
