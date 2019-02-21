from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Restaurant, ReviewPost

def index(request):
    restaurant_obj_list = Restaurant.objects.all()
    context = {"restaurant_obj_list":restaurant_obj_list,}
    print(context)
    return render(request,"review/index.html",context)

def formAddRestaurant(request):
    return render(request,'review/add_restaurant.html')

def addRestaurant(request):
    name = request.POST['name']
    address = request.POST['address']
    phone_number = request.POST['phone_number']
    Restaurant.objects.create(name=name, address=address, phone_number=phone_number)
    return HttpResponseRedirect( reverse('review:index') )

def detailRest(request, id):
    restaurant_obj = Restaurant.objects.get(pk=id)
    context = {"restaurant_obj":restaurant_obj,}
    print(context)
    return render(request,"review/index.html",context)

