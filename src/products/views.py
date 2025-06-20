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


class ProductListView(ListView):
    model = models.Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('product-title')
        serie_number = self.request.GET.get('serie-number')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        if brand:
            queryset = queryset.filter(brand_id=brand)

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = models.Brand.objects.all()
        context['categories'] = models.Category.objects.all()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request, 'products/partials/_product_table.html', context
            )
        return super().render_to_response(context, **response_kwargs)


class ProductCreateView(CreateView):
    model = models.Product
    template_name = 'products/partials/_product_form_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product-list')

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save()
        products = models.Product.objects.all()
        context = {'products': products}

        return render(self.request, 'products/partials/_product_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get("HX-Request"):
            return render(
                self.request,
                'products/partials/_product_form_create.html',
                {'form': form}
            )
        return super().form_invalid(form)


class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = 'products/partials/_product_form_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product-list')
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return render(
            request,
            self.template_name,
            {'form': form, 'product': self.get_object()}
        )

    def form_valid(self, form):
        self.object = form.save()
        products = models.Product.objects.all()
        context = {'products': products}

        return render(self.request, 'products/partials/_product_table.html', context)

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            return render(
                self.request,
                self.template_name,
                {'form': form, 'product': self.get_object()}
            )
        return super().form_invalid(form)


class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'products/partials/_product_form_delete.html'
    success_url = reverse_lazy('product-list')
    context_object_name = 'product'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if self.request.headers.get('HX-Request'):
            products = models.Product.objects.all()
            context = {'products': products}
            return render(request, 'products/partials/_product_table.html', context)

        return response

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())
