from django.forms.widgets import SelectDateWidget
from administrator.models import Post
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CategoryForm

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
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'New post created')
            return redirect('admin_home')

        context = {}
        context['form'] = form
        return render(request, 'administrator/post_create.html', context)

@login_required
def post_delete(request, id):
    p = get_object_or_404(Post, id=id, author=request.user)
    p.delete()
    messages.success(request, 'Post deleted')
    return redirect('admin_home')

@login_required
def post_edit(request, id):
    p = get_object_or_404(Post, id=id, author=request.user)

    if request.method == "GET":
        form = PostForm(instance=p)
        return render(request, 'administrator/post_create.html', {'form': form})
    
    form = PostForm(data=request.POST, instance=p, files=request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Post Updated")
        return redirect('admin_home')
    return render(request, 'administrator/post_create.html', {'form': form})

def create_category(request):
    if request.method == "GET":
        cf = CategoryForm()
        context = {}
        context['form'] = cf
        return render(request, 'administrator/category_create.html', context)