from django.shortcuts import render
from.models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Studentview(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
