from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('client/<int:order_client_id>', views.all_client_product, name='all_client_product'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/add/', views.catalog_form, name='catalog_form'),
]
