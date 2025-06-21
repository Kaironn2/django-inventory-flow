from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


class SupplierListView(LoginRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'suppliers/supplier-list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('supplier-name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request,
                'suppliers/partials/_supplier_table.html',
                context
            )
        return super().render_to_response(context, **response_kwargs)


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = models.Supplier
    template_name = 'suppliers/partials/_supplier_form_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier-list')

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save()
        suppliers = models.Supplier.objects.all()
        context = {'suppliers': suppliers}

        return render(self.request, 'suppliers/partials/_supplier_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                'suppliers/partials/_supplier_form_create.html',
                {'form': form}
            )
        return super().form_invalid(form)


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'suppliers/supplier-detail.html'
    context_object_name = 'supplier'


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Supplier
    template_name = 'suppliers/partials/_supplier_form_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier-list')
    context_object_name = 'supplier'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return render(
            request,
            self.template_name,
            {'form': form, 'supplier': self.get_object()}
        )

    def form_valid(self, form):
        self.object = form.save()
        suppliers = models.Supplier.objects.all()
        context = {'suppliers': suppliers}

        return render(self.request, 'suppliers/partials/_supplier_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request,
                self.template_name,
                {'form': form, 'supplier': self.get_object()}
            )
        return super().form_invalid(form)


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'suppliers/partials/_supplier_form_delete.html'
    success_url = reverse_lazy('supplier-list')
    context_object_name = 'supplier'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if self.request.headers.get('HX-Request'):
            supplier = models.Supplier.objects.all()
            context = {'suppliers': supplier}
            return render(request, 'suppliers/partials/_supplier_table.html', context)

        return response

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())
