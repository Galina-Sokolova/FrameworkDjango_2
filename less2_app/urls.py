from django.urls import path
from . import views

urlpatterns = [
    path('heads/', views.heads_tails, name='heads'),
    path('cub/', views.cub, name='cub'),
    path('number/', views.rand_num, name='heads'),
]
