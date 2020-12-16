from administrator.models import Post
from django.shortcuts import render, HttpResponse, get_object_or_404
import markdown

# Create your views here.
def home(request):
    context = {}
    context['posts'] = Post.objects.all().order_by('-created_on')[:30]
    return render(request, 'user/home.html', context)

def about(request):
    return render(request, 'user/about.html')

def view_post(request, url):
    p = get_object_or_404(Post, url=url)
    p.body = markdown.markdown(p.body)
    return render(request, 'user/view_post.html', {'data': p})