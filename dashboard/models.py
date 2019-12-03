from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name
    class Meta:
        ordering = ['category_name']
##BOOKS
class Book(models.Model):
    # category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE,null=True,Blank=True)
    title = models.CharField(max_length=255,unique=True)
    author = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='books')
    review = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
class User(AbstractUser):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']
    def __str__(self):
        return "{}".format(self.email)

