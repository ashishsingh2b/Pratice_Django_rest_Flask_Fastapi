from django.urls import path
from .views import BookDetailAPIView,BookListCreateAPIView

urlpatterns = [
    path("books/",BookListCreateAPIView.as_view(),name="Book-list-create"),
    path("books/<int:pk>",BookDetailAPIView.as_view(),name="book-update-delete-details")
]
