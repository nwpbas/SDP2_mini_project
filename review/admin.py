from django.contrib import admin

# Register your models here.

from .models import Restaurant, ReviewPost

admin.site.register(Restaurant)
admin.site.register(ReviewPost)