from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StudentCrud(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[BasicAuthentication]
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]