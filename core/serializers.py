from pyexpat import model
# from unicodedata import category
from rest_framework import serializers
from .models import ItemSizer, Categorias, Email, ContactUs


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    queryset = Categorias.objects.all()
    category = serializers.SlugRelatedField(
        queryset=(queryset),
        slug_field='name'
    )

    class Meta:
        model = ItemSizer
        fields = ['id', "item_pictures", "item_description", "url_amazon", "category"]



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['name']

class emailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['email']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Email.objects.create(**validated_data)

class contactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        # depth = 2

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return ContactUs.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
