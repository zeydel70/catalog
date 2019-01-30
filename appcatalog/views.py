# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404

from .models import Product, Category
from django.template import Context, Template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from helpers import *


def catalog(request, path=None):
    if path:
        categories = get_knot_category(path)
        category = categories[0]
        if is_valid_url(path, category):
            product_list = Product.objects.filter(category__in=categories)
        else:
            raise Http404
    else:
        category = None
        product_list = Product.objects.all()
    paginator = Paginator(product_list, 12)    # pagination
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalog/list_product.html', {'products': products, 'category': category})


def product(request, path, id_product):
    try:
        product = Product.objects.get(id=id_product)
    except Product.DoesNotExist:
        raise Http404
    if is_valid_url(path, product.category):
        return render(request, 'catalog/product.html', {'product': product})
    else:
        raise Http404


def search(request, path=None):
    print request.path
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            products = Product.objects.filter(name__icontains=q)
            return render(request, 'catalog/search_results.html', {'products': products, 'query': q})
    return render(request, 'catalog/search_results.html', {'errors': errors})

