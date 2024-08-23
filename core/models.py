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
    title = models.CharField(max_length=200, unique=True, default='')
    slug = models.SlugField(max_length=200, unique=True, default='')
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Categorias'


class Items(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    item_pictures = models.CharField(max_length=500, default='')
    item_description = models.CharField(max_length=100, default='')
    url_amazon = models.CharField(max_length=500, default='')
    is_especial = models.BooleanField(default=False)

    category = models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=200, default='')
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    email =models.EmailField(max_length=100)
    subject = models.CharField(max_length=200, default='')
    content = models.TextField(max_length=900,default='')
    created_on = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.email
    

class Urls(models.Model):  # Consider using singular for model names
    url = models.URLField(unique=True, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_scraped = models.DateTimeField(null=True, blank=True)
    scraped = models.BooleanField(default=False, blank=True)  # Corrected the typo
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.CharField(max_length=100, blank=True, null=True)
    product_image = models.URLField(blank=True, null=True)
    product_category = models.ManyToManyField(Categorias, blank=True)  # Removed null=True

    def __str__(self):
        return self.url
    
    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        ordering = ['-created_at']