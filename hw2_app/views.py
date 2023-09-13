import logging
from hw2_app.models import Client, Order, Product
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import CatalogForm
from django.core.files.storage import FileSystemStorage

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


def catalog(request):
    product = Product.objects.all()
    return render(request, "hw2_app/catalog.html", {'product': product})


def catalog_form(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(product_name=product_name, description=description,
                              price=price, count=count, image=image)
            product.save()
            logger.info(f'Получили {product_name=}, {price=}, {count=}.')
    else:
        form = CatalogForm()
    return render(request, 'hw2_app/catalog_form.html', {'form': form})
