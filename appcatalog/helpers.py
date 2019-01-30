# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appcatalog.models import *
from django.http import Http404


# def get_children(category):
#     categories = Category.objects.all()
#
#     children = category.child.all()
#     result = []
#     result.extend(children)
#     for child in children:
#         result.extend(get_children(child))
#     return result

categories = Category.objects.all()


def get_children(category):
    global categories
    res = []
    children = [cat for cat in categories if cat.parent_id == category.id]
    res.extend(children)
    for child in children:
        res.extend(get_children(child))
    return res


# def get_knot_category(path):
#     global categories
#     path_list = path.split('/')
#     path_list = [el for el in path_list if el]
#     try:
#         category = Category.objects.get(slug=path_list[-1])
#         return [category] + get_children(category)
#     except Category.DoesNotExist:
#         raise Http404('Category \'%s\' don\'t exist' % path_list[-1])

def get_knot_category(path):
    global categories
    path_list = path.split('/')
    path_list = [el for el in path_list if el]
    category = [cat for cat in categories if cat.slug == path_list[-1]]
    if category:
        return category + get_children(category[0])
    else:
        raise Http404('Category \'%s\' don\'t exist' % path_list[-1])


def is_valid_url(path, category):
    url = category.get_absolute_url()
    url = url.strip('/')
    return path == url

