from .serializers import SnippetSerializer
from .models import ItemSizer
from rest_framework import generics
from rest_framework import filters



class QuestionsAPIView(generics.ListCreateAPIView):
    queryset = ItemSizer.objects.all()
    serializer_class = SnippetSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = ItemSizer.objects.all()
    serializer_class = SnippetSerializer
