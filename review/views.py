from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Restaurant, ReviewPost, FoodCategory, Categorize

def index(request):
    if "restaurant_name" in request.GET:
        restaurant_obj_list = Restaurant.objects.filter(name__icontains=request.GET["restaurant_name"]).order_by('-id')
    elif "category" in request.GET:
        restaurant_obj_list = Restaurant.objects.filter(category__pk=request.GET["category"]).order_by('name')
    else:
        restaurant_obj_list = Restaurant.objects.all().order_by('-id')
    
    category_list = FoodCategory.objects.all().order_by('name')
    context = { "restaurant_obj_list":restaurant_obj_list,
                "category_list":category_list, }
    return render(request,"review/index.html",context)

def formAddRestaurant(request):
    category_list = FoodCategory.objects.all().order_by('name')
    context = {"category_list":category_list}
    return render(request,'review/add_restaurant.html', context)

def addRestaurant(request):
    name = request.POST['name']
    address = request.POST['address']
    province = request.POST['province']
    area = request.POST['area']
    sub_area = request.POST['sub_area']
    postal_code = request.POST['postal_code']
    phone_number = request.POST['phone_number']
    for val in (area, sub_area, province, postal_code):
        if len(val) != 0:
            address += " "+val
    restaurant_obj = Restaurant.objects.create(name=name, address=address, phone_number=phone_number)
    # category_obj = FoodCategory.objects.filter(name=request.POST['category'])[0]
    # category_obj = FoodCategory.objects.get(pk=request.POST['category'])
    # print(request.POST.getlist('category'))
    category_obj_list = [FoodCategory.objects.get(pk=int(id)) for id in request.POST.getlist('category') if id != ""]
    for obj in category_obj_list:
        Categorize.objects.create(restaurant=restaurant_obj, category=obj)
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




