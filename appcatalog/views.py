# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404

from appcatalog.models import Product, Category
from django.template import Context, Template
from helpers import *


def catalog(request, path=None):
    # if path:
    #     categories = get_knot_category(path)
    #     category = categories[0]
    #     if is_valid_url(path, category):
    #         product_list = Product.objects.filter(category__in=categories).order_by('id')
    #     else:
    #         raise Http404
    # else:
    #     category = None
    #     product_list = Product.objects.all().order_by('id')
    # products = paginator_products(request, product_list)
    # return render(request, 'catalog/list_product.html', {'products': products, 'category': category})
    pass


def product(request, path, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404
    if is_valid_url(path, product.category):
        return render(request, 'catalog/product.html', {'product': product})
    else:
        raise Http404


def search(request):
    print request.path
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Поиск не выполнен. Введите запрос заново')
        else:
            product_list = Product.objects.filter(name__icontains=q[:20]).order_by('id')
            products = paginator_products(request, product_list)
            return render(request, 'catalog/search_results.html', {'products': products, 'query': q})
    return render(request, 'catalog/base.html', {'errors': errors})
