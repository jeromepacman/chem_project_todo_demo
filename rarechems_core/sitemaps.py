from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.shortcuts import reverse
from django.urls import path
from apps.store.models import Category, Product


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['frontpage']

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.date_added


urlpatterns=[
    path('sitemap.xml', sitemap,
         {'sitemaps': {'flatpages': FlatPageSitemap}},
         name='django.contrib.sitemaps.views.sitemap'),
]
