
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

# Create your views here.
class BlogPostView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()