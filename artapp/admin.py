# artapp/admin.py
from django.contrib import admin
from .models import Artist, Category

admin.site.register(Artist)
admin.site.register(Category)
