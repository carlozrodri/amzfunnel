from .serializers import SnippetSerializer, CategorySerializer, emailSerializer, contactUsSerializer
from .models import Items, Categorias, Email, ContactUs, Urls
from rest_framework import generics, filters, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.tasks import scrape_urls_from_db_task
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from .serializers import UrlsSerializer


class SearchCategory(generics.ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = SnippetSerializer
    search_fields = ['category__title', 'id', 'title', 'slug', 'item_description', 'item_description1', 'item_description2', 'item_description3']
    filter_backends = (filters.SearchFilter,)
    queryset = Items.objects.all()
    permission_classes = [AllowAny]  # Allow any user to access


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Categorias.objects.all()
    permission_classes = [AllowAny]  # Allow any user to access


class CreateView(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = emailSerializer

class ContactUsView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = contactUsSerializer

# def trigger_scraping(request):
#     # This triggers the task
#     scrape_urls_from_db_task.delay()

#     return JsonResponse({'status': 'Scraping started!'})
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def urls_list_create(request):
    if request.method == 'GET':
        urls = Urls.objects.all()
        serializer = UrlsSerializer(urls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UrlsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            scrape_urls_from_db_task.delay()
            return JsonResponse({'status': 'URL added!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

