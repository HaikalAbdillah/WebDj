from django.contrib import admin
from .models import Menu, Blog

# Register your models here.

class MenuTea(admin.ModelAdmin):
    list_display = ("namaProduk", "harga")

admin.site.register(Blog, MenuTea)
admin.site.register(Menu)