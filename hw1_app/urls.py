from django.urls import path
from . import views

urlpatterns = [
    path('site/', views.first_site, name='first site'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
