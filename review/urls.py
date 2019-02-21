from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    path('', views.index, name='index'),
    path('form_add_rest/', views.formAddRestaurant, name='form_add_restaurant'),
    path('add_rest/', views.addRestaurant, name='add_restaurant'),
    path('restaurant/<int:id_rest>/', views.detailRest, name='detail'),
]