from django.contrib import admin
from .models import Slider
from .models import Categoryicons

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['sname', 'date', 'image']
    search_fields = ['sname']
    list_filter = ['date']

@admin.register(Categoryicons)
class CategoryiconsAdmin(admin.ModelAdmin):
    list_display = ['iname', 'date', 'image']
    search_fields = ['sname']
    list_filter = ['date']