from django.contrib import admin

from apps.book.models import Category, Book


admin.site.register(Category)
admin.site.register(Book)
