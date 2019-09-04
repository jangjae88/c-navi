from django.urls import path
from .views import get_blog

urlpatterns = [
    path('', get_blog, name='get_blog'),
    path('<str:search_keyword>', get_blog, name='search_result'),
]