from . import views
from django.urls import path
from .views import BlogPostView

urlpatterns = [
    path('', BlogPostView.as_view(), name='BlogPost'),
    path('<slug:slug>/', BlogPostView.as_view(), name='BlogPostView'),
]