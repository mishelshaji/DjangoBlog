from administrator.models import Post
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
@login_required
def post_list(request):
    q = Post.objects.filter(author=request.user)
    return render(request, 'administrator/home.html', {'data': q})

@login_required
def post_create(request):
    if request.method == "GET":
        context = {}
        context['form'] = PostForm()
        return render(request, 'administrator/post_create.html', context)
    
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'New post created')
            return redirect('admin_home')

        context = {}
        context['form'] = form
        return render(request, 'administrator/post_create.html', context)