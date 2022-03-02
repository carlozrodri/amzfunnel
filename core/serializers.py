from pyexpat import model
from rest_framework import serializers
from .models import ItemSizer


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemSizer
        fields = ['id', "title", "item_pictures", "item_description", "url_amazon"]


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return ItemSizer.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.save()
    #     return instance