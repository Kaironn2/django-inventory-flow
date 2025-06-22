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

from core.permissions import default_permissions

from . import forms, models


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brands/brand-list.html'
    context_object_name = 'brands'
    paginate_by = 10
    permission_required = default_permissions['brands']['view']

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('brand-name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(self.request, 'brands/partials/_brand_table.html', context)
        return super().render_to_response(context, **response_kwargs)


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brands/partials/_brand_form_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand-list')
    permission_required = default_permissions['brands']['add']

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save()
        brands = models.Brand.objects.all()
        context = {'brands': brands}

        return render(self.request, 'brands/partials/_brand_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                'brands/partials/_brand_form_create.html',
                {'form': form}
            )
        return super().form_invalid(form)


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brands/brand-detail.html'
    context_object_name = 'brand'
    permission_required = default_permissions['brands']['view']


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brands/partials/_brand_form_update.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand-list')
    context_object_name = 'brand'
    permission_required = default_permissions['brands']['change']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return render(
            request,
            self.template_name,
            {'form': form, 'brand': self.get_object()}
        )

    def form_valid(self, form):
        self.object = form.save()
        brands = models.Brand.objects.all()
        context = {'brands': brands}

        return render(self.request, 'brands/partials/_brand_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request,
                self.template_name,
                {'form': form, 'brand': self.get_object()}
            )
        return super().form_invalid(form)


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brands/partials/_brand_form_delete.html'
    success_url = reverse_lazy('brand-list')
    context_object_name = 'brand'
    permission_required = default_permissions['brands']['delete']

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if self.request.headers.get('HX-Request'):
            brands = models.Brand.objects.all()
            context = {'brands': brands}
            return render(request, 'brands/partials/_brand_table.html', context)

        return response

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())
