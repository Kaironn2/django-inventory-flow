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


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name = 'categories/category-list.html'
    context_object_name = 'categories'
    paginate_by = 10
    permission_required = default_permissions['categories']['view']

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('category-name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request,
                'categories/partials/_category_table.html',
                context
            )
        return super().render_to_response(context, **response_kwargs)


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    template_name = 'categories/partials/_category_form_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category-list')
    permission_required = default_permissions['categories']['add']

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save()
        categories = models.Category.objects.all()
        context = {'categories': categories}

        return render(self.request, 'categories/partials/_category_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                'categories/partials/_category_form_create.html',
                {'form': form}
            )
        return super().form_invalid(form)


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    template_name = 'categories/category-detail.html'
    context_object_name = 'category'
    permission_required = default_permissions['categories']['view']


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'categories/partials/_category_form_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category-list')
    context_object_name = 'category'
    permission_required = default_permissions['categories']['change']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return render(
            request,
            self.template_name,
            {'form': form, 'category': self.get_object()}
        )

    def form_valid(self, form):
        self.object = form.save()
        categories = models.Category.objects.all()
        context = {'categories': categories}

        return render(self.request, 'categories/partials/_category_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request,
                self.template_name,
                {'form': form, 'category': self.get_object()}
            )
        return super().form_invalid(form)


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'categories/partials/_category_form_delete.html'
    success_url = reverse_lazy('category-list')
    context_object_name = 'category'
    permission_required = default_permissions['categories']['delete']

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if self.request.headers.get('HX-Request'):
            categories = models.Category.objects.all()
            context = {'categories': categories}
            return render(request, 'categories/partials/_category_table.html', context)

        return response

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())
