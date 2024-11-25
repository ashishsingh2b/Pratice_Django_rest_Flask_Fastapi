from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import (ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin)
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookListCreateView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
class BookDetailView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Book.objects.all()
    serializer_class=BookSerializer


    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)
