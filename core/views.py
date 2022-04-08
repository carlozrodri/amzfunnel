from .serializers import SnippetSerializer, CategorySerializer, emailSerializer
from .models import ItemSizer, Categorias, Email
from rest_framework import generics, filters, viewsets


class QuestionsAPIView(generics.ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = SnippetSerializer
    search_fields = ['category__name']
    filter_backends = (filters.SearchFilter,)
    queryset = ItemSizer.objects.all()

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Categorias.objects.all()

class CreateView(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = emailSerializer
   