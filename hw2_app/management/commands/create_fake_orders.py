from django.core.management.base import BaseCommand

from hw2_app.models import Client, Product, Order
from random import randint


class Command(BaseCommand):
    help = "Generate fake orders. Command: python manage.py create_fake_orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count orders')

    def handle(self, *args, **kwargs):
        number_users = len(Client.objects.all())
        number_products = len(Product.objects.all())
        count = kwargs.get('count')
        for k in range(1, count + 1):
            order_client = Client.objects.get(id=randint(1, number_users + 1))
            order = Order(order_client=order_client, total_price=0)
            order.save()
            selected_products = []
            for i in range(1, 5):
                temp = randint(1, number_products)
                product = Product.objects.get(pk=temp)
                selected_products.append(product)
            for product in selected_products:
                order.order_product.add(product)
            order.total_price = sum(product.price for product in selected_products)
            order.save()

        self.stdout.write('Fake orders added')
