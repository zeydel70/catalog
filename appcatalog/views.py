# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render

from .models import Product, Category
from django.template import Context, Template

def catalog(request, slug=None):
    return render(request, 'catalog/content.html',  context=RequestContext(request)) #

# def category(request, path):
#     '/'
#     '/monitors/19/'
#
#
#     return render(request, 'catalog/category.html', {"categories": get_object_or_404(Category, slug=slug)})