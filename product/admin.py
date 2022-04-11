from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display=['title', 'updated','timestamp']
    list_display_links=['title']
    list_filter=['updated','timestamp','title']
    search_fields=['title','description']
admin.site.register(Product, ProductAdmin)