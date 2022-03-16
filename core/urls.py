from django.urls import path, include
from .views import QuestionsAPIView, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorias', CategoryViewSet, 'categorias')
urlpatterns = [
    path('', QuestionsAPIView.as_view()),
    path('', include(router.urls)),
]
