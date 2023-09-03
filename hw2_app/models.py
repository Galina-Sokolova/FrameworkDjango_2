from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.client_name}, email: {self.email}, phone number: {self.phone_number},' \
               f' address: {self.address}, registration date: {self.registration_date}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.ImageField()
    date_added_product = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.product_name}, description: {self.description}, price: {self.price},' \
               f' count: {self.count},date the item was added: {self.date_added_product}'


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_product = models.ManyToManyField(Product)
    date_order = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Customer: {self.order_client}, product: {self.order_product}, date order: {self.date_order},' \
               f' total price: {self.total_price}'
