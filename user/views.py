from administrator.models import Post
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'user/home.html')

def about(request):
    return render(request, 'user/about.html')

def view_post(request, url):
    p = Post.objects.get(url=url)
    return render(request, 'user/view_post.html', {'data': p})