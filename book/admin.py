from django.contrib import admin

from .models import Category, Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(Category)