from django.urls import path,include
from rest_framework import routers
from . views import *

router = routers.DefaultRouter()
router.register('categories', CategoryViewset)
router.register('books', BookViewset)

urlpatterns = [
  path('',include(router.urls))  
]