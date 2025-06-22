from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework import generics

from core.permissions import default_permissions

from . import forms, models, serializers


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'suppliers/supplier-list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = default_permissions['suppliers']['view']

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


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supplier
    template_name = 'suppliers/partials/_supplier_form_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier-list')
    permission_required = default_permissions['suppliers']['add']

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


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'suppliers/supplier-detail.html'
    context_object_name = 'supplier'
    permission_required = default_permissions['suppliers']['view']


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supplier
    template_name = 'suppliers/partials/_supplier_form_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier-list')
    context_object_name = 'supplier'
    permission_required = default_permissions['suppliers']['change']

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


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'suppliers/partials/_supplier_form_delete.html'
    success_url = reverse_lazy('supplier-list')
    context_object_name = 'supplier'
    permission_required = default_permissions['suppliers']['delete']

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


class SupplierCreateListView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
