# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appcatalog.models import *
from django.http import Http404


# def get_children(category):
#     '''
#     :param category: type String - name  of category
#     :return: list of children for this category
#
#     '''
#
#     if Category.objects.filter(parent__name=slug_category):
#         result = list(Category.objects.filter(parent__name=slug_category))
#         for item in result:
#             tmp = []
#             tmp.append(get_children(item))
#         if any(tmp):
#             result += tmp
#         else:
#             return result
#     else:
#         return []


def get_children(category):
    children = category.child.all()
    result = []
    result.extend(children)
    for child in children:
        result.extend(get_children(child))
    return result


def get_knot_category(path):
    path_list = path.split('/')
    path_list = [el for el in path_list if el]
    try:
        category = Category.objects.get(slug=path_list[-1])
        return [category] + get_children(category)
    except Category.DoesNotExist:
        raise Http404('Category \'%s\' don\'t exist' % path_list[-1])


def is_valid_url(path, category):
    url = category.get_absolute_url()
    url = url.strip('/')
    return path == url

