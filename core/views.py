from .serializers import SnippetSerializer, CategorySerializer, emailSerializer, contactUsSerializer
from .models import Items, Categorias, Email, ContactUs
from rest_framework import generics, filters, viewsets

class SearchCategory(generics.ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = SnippetSerializer
    search_fields = ['category__title', 'id', 'title', 'item_description', 'item_description1', 'item_description2', 'item_description3']
    filter_backends = (filters.SearchFilter,)
    queryset = Items.objects.all()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Categorias.objects.all()

class CreateView(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = emailSerializer

class ContactUsView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = contactUsSerializer