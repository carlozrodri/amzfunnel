from email.policy import default
from django.db import models

class Email(models.Model):
    email = models.EmailField(max_length=100 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email



class Categorias(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')        
    slug = models.SlugField(max_length=200, default='')
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ItemSizer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    item_pictures = models.CharField(max_length=500, default='')
    item_description = models.CharField(max_length=100, default='')
    url_amazon = models.CharField(max_length=500, default='')
    category = models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    email =models.EmailField(max_length=100, unique=True, default='')
    subject = models.CharField(max_length=200, default='')
    content = models.TextField(max_length=900, unique=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name