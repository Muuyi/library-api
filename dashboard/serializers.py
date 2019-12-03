from rest_framework import serializers
from . models import *
##CATEGORIES
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
##BOOK SERIALIZER
class BookSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = Book
        fields = '__all__'