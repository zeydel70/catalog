# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appcatalog.models import *


def get_children(slug_category):
    '''
    :param category: type String - name  of category
    :return: list of children for this category

    '''

    if Category.objects.filter(parent__name=slug_category):
        result = list(Category.objects.filter(parent__name=slug_category))
        for item in result:
            tmp = []
            tmp.append(get_children(item))
        if any(tmp):
            result += tmp
        else:
            return list(Category.objects.filter(name=category)) + result
    else:
        return []