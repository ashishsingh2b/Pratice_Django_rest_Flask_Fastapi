from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, UserValidationAPIView, LoginAPIView, ArticleViewSet

# Router for CRUD API (Articles)
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)  # Register the ArticleViewSet for CRUD operations

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),  # User Registration API
    path('validate/<int:user_id>/', UserValidationAPIView.as_view(), name='validate_user'),  # Admin validation API
    path('login/', LoginAPIView.as_view(), name='login'),  # User Login API (JWT)
    path('api/', include(router.urls)),  # Include URLs for the CRUD API (articles)
]
