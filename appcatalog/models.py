# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=128)
    img = models.ImageField(upload_to='images', blank=True, help_text = '100x100px')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    description = models.TextField(max_length=300)

    def __str__(self):
        return '%s' % self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=50, )
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child')
    description = models.TextField(max_length=300)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        if self.parent is None:
            url = '/{}/'.format(self.slug)
            return url
        else:
            return '{}{}/'.format(self.parent.get_absolute_url(), self.slug)
