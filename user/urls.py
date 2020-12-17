from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('about/', about, name='aboutpage'),
    path('search/', search_post, name='searchpost'),
    path('<str:url>/', view_post, name='viewpost'),
]