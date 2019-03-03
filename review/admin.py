from django.contrib import admin

# Register your models here.

from .models import Restaurant, ReviewPost, FoodCategory

admin.site.register(Restaurant)
admin.site.register(ReviewPost)
admin.site.register(FoodCategory)