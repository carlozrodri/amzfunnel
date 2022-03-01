from rest_framework import serializers
from .models import ItemSizer


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    item_pictures = serializers.CharField(max_length=500, default='')
    item_description = serializers.CharField(max_length=100, default='')
    url_amazon = serializers.CharField(max_length=500, default='')


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