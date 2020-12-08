from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='admin_home'),
    path('post/create/', post_create, name='admin_post_create'),
]