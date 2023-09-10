import logging
from hw2_app.models import Client, Order, Product
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

logger = logging.getLogger(__name__)


def base(request):
    logger.info('Index page accessed')
    return render(request, "base.html")


def contacts(request):
    form = """<div class="row">
        <li class="nav-item"><a href="/online_shop/base/"
            class="nav-link">Главная</a></li>
            <h1>Contact: </h1>
            <p>Email: pol@mail.ru</p>
            <p>Phone: +7-999-777-11-11</p>
        </div>
        """
    logger.info('Visited the page contacts')
    return HttpResponse(form)


def all_client_product(request, order_client_id):
    client = get_object_or_404(Client, pk=order_client_id)
    orders = Order.objects.filter(order_client_id=order_client_id).all()
    products = set(product for order in orders for product in order.order_product.values_list('product_name'))

    return render(request, 'hw2_app/all_client_product.html', {'client': client,
                                                               'orders': orders,
                                                               'products': products})
