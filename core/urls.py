from django.urls import path, include
from .views import SearchCategory, CategoryViewSet, CreateView, ContactUsView, urls_list_create, task_status
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorias', CategoryViewSet, 'categorias')
urlpatterns = [
    path('', SearchCategory.as_view(), name='search_category'),
    path('', include(router.urls), name='categorias'),
    path('email', CreateView.as_view(), name='email'),
    path('contactus', ContactUsView.as_view(), name='contactus'),
    # path('categorias', CategoryViewSet.as_view({'get': 'list'})),
    path('urls/', urls_list_create, name='urls_list_create'),
    path('task-status/<str:task_id>/', task_status, name='task_status'),
]
