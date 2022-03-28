from csv import list_dialects
from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
   list_display = ["__str__", "price", "slug"]
   prepopulated_fields = {'slug': ('title', )}
   
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)