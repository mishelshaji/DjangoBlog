from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='admin_home'),
    path('post/create/', post_create, name='admin_post_create'),
    path('post/edit/<int:id>/', post_edit, name='admin_post_edit'),
    path('post/delete/<int:id>/', post_delete, name='admin_post_delete'),
    path('category/', category_list, name='admin_category_list'),
    path('category/create/', create_category, name='admin_category_create'),
]