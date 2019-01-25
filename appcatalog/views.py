# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from django.http import Http404

from .models import Product, Category
from django.template import Context, Template
from helpers import *


def catalog(request, path=None):
    if path:
        path_list = path.split('/')
        path_list = [el for el in path_list if el]
        try:
            abs_url = Category.objects.get(slug=path_list[-1]).get_absolute_url()
            abs_url = abs_url.strip('/')
        except Category.DoesNotExist:
            raise Http404
        if path == abs_url:
            products = Product.objects.filter(category__in=get_knot_category(Category.objects.get(slug=path_list[-1])))
        else:
            raise Http404
    else:
        products = Product.objects.all()
    return render(request, 'catalog/content.html', {'products': products})