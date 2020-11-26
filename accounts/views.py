from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def user_login(request):
    return render(request, 'accounts/login.html', {"form": AuthenticationForm()})