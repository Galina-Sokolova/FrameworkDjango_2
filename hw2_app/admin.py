from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'count']
    ordering = ['price', '-count']
    list_filter = ['date_added_product', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]


admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
