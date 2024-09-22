from pyexpat import model
# from unicodedata import category
from rest_framework import serializers
from .models import Items, Categorias, Email, ContactUs, Urls


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    queryset = Categorias.objects.all()
    category = serializers.SlugRelatedField(
        queryset=(queryset),
        slug_field='title'
    )

    class Meta:
        model = Items
        fields = ['id', "item_pictures", 'slug' , "item_description", "url_amazon", "category", "created", "updated", "title", "item_description1", "item_description2", "item_description3", "is_especial", "asin"]

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = ['id', 'url']  # Include the fields you want in the API

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['title', 'slug']

# new serializers
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['id', 'title']

class UrlsSerializer(serializers.ModelSerializer):
    product_category = CategoriaSerializer(many=True, read_only=True)

    class Meta:
        model = Urls
        fields = ['id', 'url', 'created_at', 'updated_at', 'last_scraped', 'scraped',
                  'product_name', 'product_description', 'product_price',
                  'product_image', 'product_category']


# ------
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

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ContactUs.objects.create(**validated_data)
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
