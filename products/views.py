from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.cache import cache

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store - Home'


class ProductListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Catalog'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')

        if category_id:
            return queryset.filter(category_id=category_id)
        else:
            return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        categories = cache.get('categories')
        if not categories:
            context['categories'] = ProductCategory.objects.all()
            cache.set('categories', context['categories'], timeout=90)
        else:
            context['categories'] = ProductCategory.objects.all()
        return context


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


# def products(request, category_id=None, page_number=1):
#
#     if category_id:
#         requested_products = Product.objects.filter(category_id=category_id)
#     else:
#         requested_products = Product.objects.all()
#
#     paginator = Paginator(requested_products, 3)
#     products_paginator = paginator.page(page_number)
#
#     context = {
#         'title': 'Store - Catalog',
#         'categories': ProductCategory.objects.all(),
#         'products': products_paginator
#     }
#
#     return render(request, 'products/products.html', context)
