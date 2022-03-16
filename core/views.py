from .serializers import SnippetSerializer, CategorySerializer
from .models import ItemSizer, Categorias
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets


class QuestionsAPIView(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = SnippetSerializer
    search_fields = ['category__name']
    filter_backends = (filters.SearchFilter,)
    queryset = ItemSizer.objects.all()
    serializer_class = SnippetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Categorias.objects.all()
