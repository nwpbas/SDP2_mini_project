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

def detailRest(request, id_rest):
    restaurant_obj = Restaurant.objects.get(pk=id_rest)
    all_review_obj = ReviewPost.objects.filter(restaurant_id=id_rest).order_by('-timestamp')
    context = {'restaurant_obj':restaurant_obj,
                'all_review_obj':all_review_obj,}  
    return render(request,"review/detail.html",context)

def formWriteReview(request, id_rest):
    restaurant_obj = Restaurant.objects.get(pk=id_rest)
    context = {'restaurant_obj':restaurant_obj,} 
    return render(request,'review/write_review.html',context)

def addReview(request):
    print(request.POST)
    restaurant_obj = Restaurant.objects.get(pk=request.POST['restaurant_id'])
    r_topic = request.POST['review_topic'] 
    r_detail = request.POST['review_detail']
    rating = request.POST['rating']
    restaurant_obj.reviewpost_set.create(review_topic=r_topic, review_datail=r_detail, rating=rating)
    return HttpResponseRedirect( reverse('review:detail', args=(request.POST['restaurant_id'],)) )




