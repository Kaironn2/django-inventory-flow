from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from core.permissions import default_permissions

from . import forms, models


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflows/inflow-list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = default_permissions['inflows']['view']

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(self.request, 'inflows/partials/_inflow_table.html', context)
        return super().render_to_response(context, **response_kwargs)


class InflowCreateView(LoginRequiredMixin, CreateView):
    model = models.Inflow
    template_name = 'inflows/partials/_inflow_form_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow-list')
    permission_required = default_permissions['inflows']['add']

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save()
        inflows = models.Inflow.objects.all()
        context = {'inflows': inflows}

        return render(self.request, 'inflows/partials/_inflow_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                'inflows/partials/_inflow_form_create.html',
                {'form': form}
            )
        return super().form_invalid(form)


class InflowDetailView(LoginRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflows/inflow-detail.html'
    context_object_name = 'inflow'
    permission_required = default_permissions['inflows']['view']
