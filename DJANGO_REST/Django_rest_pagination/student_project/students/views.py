from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination


# class StudentPagination(PageNumberPagination):
#     page_size = 5  # Define the page size here
#     page_size_query_param = 'page_size'  # Allow users to override page size in the query string
#     max_page_size = 100  # Maximum number of items per page (optional)
#     page_query_param = 'page'  # Allow users to override page number in the query string
#     last_page_string= 'end'

# from rest_framework.pagination import LimitOffsetPagination

# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5  # Default number of items per request
#     max_limit = 100  # Maximum number of items allowed


from rest_framework.pagination import CursorPagination

class MyCursorpagination(CursorPagination):
    page_size= 5
    ordering = 'id'  # Ordering the data in descending order

    


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = StudentPagination
    # pagination_class = MyLimitOffsetPagination
    pagination_class=MyCursorpagination
    

