from django.urls import path
from .views import *

urlpatterns = [
    path('login', user_login, name='login'),
]