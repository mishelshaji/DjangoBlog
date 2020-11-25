from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'user/home.html')

def about(request):
    return render(request, 'user/about.html')