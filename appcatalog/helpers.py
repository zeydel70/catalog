# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appcatalog.models import *
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_children(category, categories):
    res = []
    children = [cat for cat in categories if cat.parent_id == category.id]
    res.extend(children)
    for child in children:
        res.extend(get_children(child, categories))
    return res


def get_knot_category(path):
    path_list = path.split('/')
    path_list = [el for el in path_list if el]
    categories = Category.objects.all()
    category = [cat for cat in categories if cat.slug == path_list[-1]]
    if category:
        return category + get_children(category[0], categories)
    else:
        raise Http404('Category \'%s\' don\'t exist' % path_list[-1])


def is_valid_url(path, category):
    url = category.get_absolute_url()
    url = url.strip('/')
    return path == url


def paginator_products(request, list_objects):
    paginator = Paginator(list_objects, 12)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects

