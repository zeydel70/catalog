# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.exceptions import ValidationError
# from helpers import get_level_category
# from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=128)
    img = models.ImageField(upload_to='images', blank=True, help_text='100x100px')
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    description = models.TextField(max_length=300)

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        url = '%sproduct/%s/' % (self.category.get_absolute_url(), self.slug)
        return url

    def get_img(self):
        if self.img:
            return self.img
        return self.category.get_img()


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child')
    img = models.ImageField(upload_to='images', blank=True, help_text='category_image')
    description = models.TextField(max_length=300)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s' % self.name

    def clean(self):
        if get_level_category(self.parent) == 3:
            raise ValidationError({'parent': 'Dont\'t use category greater 3 level'})

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
        return reversed(self.prepare_breadcrumb())


def generate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)


pre_save.connect(generate_slug, sender=Product)
