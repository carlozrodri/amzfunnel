
from email.policy import default
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



class ItemSizer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    item_pictures = models.CharField(max_length=500, default='')
    item_description = models.CharField(max_length=100, default='')
    url_amazon = models.CharField(max_length=500, default='')

    class Meta:
        ordering = ['title']