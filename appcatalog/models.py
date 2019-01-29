# -*- coding: utf-8 -*-

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    img = models.ImageField(upload_to='images', blank=True, help_text='100x100px')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    description = models.TextField(max_length=300)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        url = '%sproduct/%s/' % (self.category.get_absolute_url(), self.id)
        return url

    def get_img(self):
        if self.img:
            return self.img
        return self.category.get_img()

    def breadcrumb(self):
        res = list(self.category.breadcrumb())
        res.append((self.name, self.get_absolute_url()))
        return res


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=50, )
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child')
    img = models.ImageField(upload_to='images', blank=True, help_text='category_image')
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

    def get_img(self):
        if self.img:
            return self.img
        return self.parent.get_img()

    def prepare_breadcrumb(self):
        url = []
        url.append((self.name, self.get_absolute_url()))
        if self.parent is None:
            return url
        else:
            url += self.parent.prepare_breadcrumb()
        return url

    def breadcrumb(self):
        return list(reversed(self.prepare_breadcrumb()))


