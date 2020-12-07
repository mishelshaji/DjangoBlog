from django.urls import path
from .views import *

urlpatterns = [
    path('post/', post_list, name='admin_post_list'),
    path('post/create/', post_create, name='admin_post_create'),
]