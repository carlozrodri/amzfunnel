from email.policy import default
from django.db import models

class Email(models.Model):
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email



class Categorias(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
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
    is_especial = models.BooleanField(default=False)
    category = models.ForeignKey(
        Categorias,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
