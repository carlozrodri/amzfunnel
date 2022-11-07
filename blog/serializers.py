from pyexpat import model
# from unicodedata import category
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
         'title',
         'slug',
         'author',
         'content',
         'created_on', 
         'post_picture_0',
         'post_picture_1',
         'post_picture_2',
         'title_thumbnail',
         'thumbnail_picture'
         )
