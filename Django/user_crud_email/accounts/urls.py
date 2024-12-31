from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
]
