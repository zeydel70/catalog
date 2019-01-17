# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product


# def hello(request):
#    return render(request, 'cat_templ/main.html', locals())

def index(request):
    products = Product.objects.all()
    return render(request, 'cat_templ/main.html', {"products": products})

