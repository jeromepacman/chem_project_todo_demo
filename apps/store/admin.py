from django.contrib import admin

from .models import Category, Product, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'category', 'parent', 'is_featured', 'price', 'num_available', 'num_visits')
    list_filter=('category', 'is_featured', 'num_visits')
    prepopulated_fields={'slug': ('title', 'quantity', 'unit')}


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview)
