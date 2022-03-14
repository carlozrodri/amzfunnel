from .serializers import SnippetSerializer
from .models import ItemSizer, Categorias
from rest_framework import generics
from rest_framework import filters



class QuestionsAPIView(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = SnippetSerializer
    search_fields = ['category__name']
    filter_backends = (filters.SearchFilter,)
    queryset = ItemSizer.objects.all()
    serializer_class = SnippetSerializer
