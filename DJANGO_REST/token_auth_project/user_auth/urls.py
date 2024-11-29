from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Studentview  # Make sure this is a ViewSet class
from rest_framework.authtoken.views import obtain_auth_token

# Create a router instance
router = DefaultRouter()
router.register(r'student', Studentview, basename='student')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('auth',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token)

]
