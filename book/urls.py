from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='book_home'),
    path('create/', new_book, name='book_create'),
    path('update/<int:id>', update_book, name='book_update'),
]