from django.core.management.base import BaseCommand
from hw2_app.models import Product


class Command(BaseCommand):
    help = "Add product."

    def add_arguments(self, parser):
        parser.add_argument('product_name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Description od product')
        parser.add_argument('price', type=float, help='Price of product')
        parser.add_argument('count', type=int, help='Count of product')

    def handle(self, *args, **kwargs):
        product = Product(product_name=kwargs.get('product_name'),
                          description=kwargs.get('description'),
                          price=kwargs.get('price'),
                          count=kwargs.get('count')
                          )
        product.save()
        self.stdout.write(f'{product}')
