from django.contrib import admin

# Register your models here.

from .models import Stores, Products

admin.site.register(Stores)
admin.site.register(Products)

