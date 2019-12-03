from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from . serializers import *
# Create your views here.
##CATEGORY VIEWSET
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
##BOOK VIEWSET
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer