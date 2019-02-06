# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appcatalog.models import Category
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def get_children(category, categories):
#     res = []
#     children = [cat for cat in categories if cat.parent_id == category.id]
#     res.extend(children)
#     for child in children:
#         res.extend(get_children(child, categories))
#     return res


def get_children(category, categories):
    children_category = []
    children = [[cat] for cat in categories if cat.parent_id == category.id]
    children_category.extend(children)
    for child in children:
        child.append(get_children(child[0], categories))
    return children_category


def tree_categories():
    tree = []
    categories = Category.objects.all()
    for root in [category for category in categories if category.parent_id is None]:
        branch_category = [root, get_children(root, categories)]
        tree.append(branch_category)
    return tree


def get_valid_category(path):
    path_list = path.split('/')
    path_list = [el for el in path_list if el]
    tree = tree_categories()

    return None

    # categories = Category.objects.all()
    # category = [cat for cat in categories if cat.slug == path_list[-1]]
    # if category:
    #     return category + get_children(category[0], categories)
    # else:
    #     raise Http404('Category \'%s\' don\'t exist' % path_list[-1])


def get_level_category(category):
    level = 1
    if category.parent:
        return level + get_level_category(category.parent)
    return level


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

