from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('about/', about, name='aboutpage'),
    path('<str:url>/', view_post, name='viewpost'),
]