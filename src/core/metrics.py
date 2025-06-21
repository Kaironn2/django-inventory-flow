from django.db.models import Count, F, FloatField, Sum
from django.utils import timezone

from brands.models import Brand
from categories.models import Category
from outflows.models import Outflow
from products.models import Product


class Metrics:

    @staticmethod
    def get_products_metrics():
        aggregate = Product.objects.aggregate(
            total_cost_price=Sum(
                F('cost_price') * F('quantity'), output_field=FloatField()
            ),
            total_selling_price=Sum(
                F('selling_price') * F('quantity'), output_field=FloatField()
            ),
            total_quantity=Sum('quantity'),
        )

        total_cost_price = aggregate.get('total_cost_price') or 0
        total_selling_price = aggregate.get('total_selling_price') or 0
        total_quantity = aggregate.get('total_quantity') or 0
        total_profit = (
            aggregate.get('total_selling_price') - aggregate.get('total_cost_price')
            or 0
        )

        return dict(
            total_cost_price=total_cost_price,
            total_selling_price=total_selling_price,
            total_quantity=total_quantity,
            total_profit=total_profit,
        )

    @staticmethod
    def get_sales_metrics():
        aggregate = Outflow.objects.aggregate(
            total_products_sold=Sum('quantity'),
            total_sales_value=Sum(F('quantity') * F('product__selling_price')),
            total_sales_cost=Sum(F('quantity') * F('product__cost_price')),
        )

        total_sales = Outflow.objects.count() or 0
        total_products_sold = aggregate.get('total_products_sold') or 0
        total_sales_value = aggregate.get('total_sales_value') or 0
        total_sales_profit = (
            aggregate.get('total_sales_value') - aggregate.get('total_sales_cost')
        ) or 0

        return dict(
            total_sales=total_sales,
            total_products_sold=total_products_sold,
            total_sales_value=total_sales_value,
            total_sales_profit=total_sales_profit,
        )

    @staticmethod
    def get_daily_sales_data():
        today = timezone.now().date()
        dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
        values = []

        for date in dates:
            sales_total = Outflow.objects.filter(
                created_at__date=date
            ).aggregate(
                total_sales=Sum(F('product__selling_price') * F('quantity'))
            )['total_sales'] or 0
            values.append(float(sales_total))

        return dict(
            dates=dates,
            values=values,
        )

    @staticmethod
    def get_daily_sales_quantity_data():
        today = timezone.now().date()
        dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
        values = [
            Outflow.objects.filter(created_at__date=date).count() for date in dates
        ]

        return dict(
            dates=dates,
            values=values,
        )

    @staticmethod
    def get_product_by_category_data():
        category_product_count = (
            Category.objects
            .annotate(product_count=Count('products'))
            .values_list('name', 'product_count')
        )
        return dict(category_product_count)

    @staticmethod
    def get_product_by_brand_data():
        brand_product_count = (
            Brand.objects
            .annotate(product_count=Count('products'))
            .values_list('name', 'product_count')
        )
        return dict(brand_product_count)
