from pyexpat import model
# from unicodedata import category
from rest_framework import serializers
from .models import ItemSizer, Categorias


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    queryset = Categorias.objects.all()
    category = serializers.SlugRelatedField(
        queryset=(queryset),
        slug_field='name'
    )
    
    class Meta:
        model = ItemSizer
        fields = ['id', "title", "item_pictures", "item_description", "url_amazon", "category"]


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ItemSizer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance