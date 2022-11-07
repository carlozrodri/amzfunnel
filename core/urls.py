from django.urls import path, include
from .views import QuestionsAPIView, CategoryViewSet, CreateView, ContactUsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorias', CategoryViewSet, 'categorias')
urlpatterns = [
    path('', QuestionsAPIView.as_view()),
    path('', include(router.urls)),
    path('email', CreateView.as_view()),
    path('contactus', ContactUsView.as_view())
    # path('categorias', CategoryViewSet.as_view({'get': 'list'})),
]
