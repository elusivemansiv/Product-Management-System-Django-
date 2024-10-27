from django.contrib import admin
from .models import Casing,Gpu

@admin.register(Casing)
class CasingAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_model', 'price', 'color', 'date', 'slug'] 
    prepopulated_fields = {'slug': ('product_name',)}  


@admin.register(Gpu)
class GpuAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_model', 'price', 'color', 'date', 'slug'] 
    prepopulated_fields = {'slug': ('product_name',)} 

