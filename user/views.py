from administrator.models import Post
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
import markdown

# Create your views here.
def home(request):
    context = {}
    context['posts'] = Post.objects.all().select_related('author').order_by('-created_on')[:30]
    return render(request, 'user/home.html', context)

def about(request):
    return render(request, 'user/about.html')

def view_post(request, url):
    p = get_object_or_404(Post, url=url)
    p.body = markdown.markdown(p.body)
    return render(request, 'user/view_post.html', {'data': p})

def search_post(request):
    search = request.GET.get('q')
    if search is None:
        return redirect('user_home')
    
    context = {}
    context['posts'] = Post.objects.filter(title__contains=search).order_by('-created_on')[:30]
    return render(request, 'user/home.html', context)
