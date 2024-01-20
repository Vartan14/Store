from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage

from products.models import ProductCategory, Product, Basket


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):

    if category_id:
        requested_products = Product.objects.filter(category_id=category_id)
    else:
        requested_products = Product.objects.all()

    paginator = Paginator(requested_products, 3)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }

    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(product=product, user=request.user)

    if not baskets.exists():
        Basket.objects.create(product=product, user=request.user, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id, user=request.user)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

