from django import forms

from hw2_app import models


class CatalogForm(forms.Form):
    product_name = forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Описание продукта'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Цена'}))
    count = forms.IntegerField(max_value=10000, widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Количество'}))
    image = forms.ImageField()
