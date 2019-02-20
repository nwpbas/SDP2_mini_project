from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name   

class ReviewPost(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_topic = models.CharField(max_length=200)
    review_datail = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# class FoodCategory(models.Model):
#     category = models.CharField(max_length=200)



