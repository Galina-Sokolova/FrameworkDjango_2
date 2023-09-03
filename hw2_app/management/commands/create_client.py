from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        client = Client(client_name='Petr', email='petr@example.com',
                        phone_number='+79127633765', address='Kaluga')
        client.save()
        self.stdout.write(f'{client}')
