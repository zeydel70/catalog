# -*- coding: utf-8 -*-

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    img = models.ImageField(upload_to = 'images', blank=True, help_text = '100x100px')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    description = models.TextField(max_length=300)


    def __str__(self):
        return '%s' % self.name

class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child')
    description = models.TextField(max_length=300)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

 # print Category.objects.all().query