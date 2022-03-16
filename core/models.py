from email.policy import default
from django.db import models


class Categorias(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')

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
