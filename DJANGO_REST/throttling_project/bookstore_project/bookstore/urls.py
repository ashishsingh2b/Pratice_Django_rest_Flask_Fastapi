from django.urls import path,include
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List and Create
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, Update, Delete
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete
    path('login/',include('rest_framework.urls'))

]



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('login/',include('rest_framework.urls'))
    
# ]
