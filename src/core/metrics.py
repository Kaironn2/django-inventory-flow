from django.db.models import F, FloatField, Sum

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
                F('cost_price') * F('quantity'), output_field=FloatField()
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
            total_sales_value=Sum(F('quantity') * F('product.selling_price')),
            total_sales_cost=Sum(F('quantity') * F('product.cost_price'))
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
