from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import StudentCrud
from rest_framework import routers

router= DefaultRouter()

router.register(r'student',StudentCrud)

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]
