from django.shortcuts import render
from .models import Book
from .serializers import BookSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import request
# Create your views here.

class BookListCreateAPIView(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializers(books,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BookDetailAPIView(APIView):
    def get(self,request,pk):
        try:
            book=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error":"Book not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=BookSerializers(book)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            book=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error":"Book not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=BookSerializers(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            book=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error":"Book not Found"},status=status.HTTP_404_NOT_FOUND)
        
        book.delete()   
        return Response({"Message":"Book Deleted"},status=status.HTTP_204_NO_CONTENT)
            
    
