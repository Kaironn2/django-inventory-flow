from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from . import forms, models


class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflows/outflow-list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product-title')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request, 'outflows/partials/_outflow_table.html', context
            )
        return super().render_to_response(context, **response_kwargs)


class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflows/partials/_outflow_form_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow-list')

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save()
        outflows = models.Outflow.objects.all()
        context = {'outflows': outflows}

        return render(self.request, 'outflows/partials/_outflow_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                'outflows/partials/_outflow_form_create.html',
                {'form': form}
            )
        return super().form_invalid(form)


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflows/outflow-detail.html'
    context_object_name = 'outflow'
