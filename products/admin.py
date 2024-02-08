from django.contrib import admin
from django.contrib.admin import ModelAdmin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')

    # readonly_fields = ('description', )
    search_fields = ('name',)

    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_at')
    readonly_fields = ('created_at',)
    extra = 0
