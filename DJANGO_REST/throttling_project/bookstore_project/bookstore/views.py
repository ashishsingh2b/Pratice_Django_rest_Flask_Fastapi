from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
#from .throttling import RequestCountThrottle
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import Jackratethrottel

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     # throttle_classes = [AnonRateThrottle, ContactDetailView]  # Apply throttling
#     throttle_classes = [Jackratethrottel]  # Apply throttling
#     # throttle_classes = [AnonRateThrottle,UserRateThrottle]

#    # throttle_classes = [RequestCountThrottle]  # Apply custom throttle

#     # def perform_create(self, serializer):
#     #     # Optional: Log the request when creating a book
#     #     serializer.save(user=self.request.user)


#crud manual


from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.throttling import ScopedRateThrottle

# View to list all books and create a new book
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'lsit'

# View to retrieve, update or delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'detail'

# View to create a new book (separated for clarity, as create operation is handled in BookListView)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create'

# View to update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'update'

# View to delete an existing book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'delete'


