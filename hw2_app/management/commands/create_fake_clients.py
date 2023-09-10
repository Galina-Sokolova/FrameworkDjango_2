from django.core.management.base import BaseCommand

from hw2_app.models import Client
from random import randint
import random


class Command(BaseCommand):
    help = "Generate fake users. Command: python manage.py create_fake_users number_users"

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of users')

    def handle(self, *args, **kwargs):
        address_list = ["Moscow", "Kaluga", "Tula", "Astrakhan", "Ufa", "Saint Petersburg"]
        number = kwargs.get('number')
        for i in range(1, number + 1):
            user = Client(client_name=f'Username_{i}',
                          email=f'mail{i}@mail.ru',
                          phone_number=f'8-800-{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}',
                          address=f'{random.choice(address_list)}')
            user.save()
        self.stdout.write("Generate fake users completed.")
