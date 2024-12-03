# music/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SingerViewSet, SongViewSet

router = DefaultRouter()
router.register(r'singers', SingerViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
