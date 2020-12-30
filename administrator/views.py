from django.forms.widgets import SelectDateWidget
from administrator.models import Category, Post
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CategoryForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# @login_required
# def post_list(request):
#     q = Post.objects.filter(author=request.user)
#     return render(request, 'administrator/home.html', {'data': q})

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "administrator/home.html"
    # queryset = Post.objects.all()
    context_object_name = 'data'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

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

@login_required
def create_category(request):
    if request.method == "GET":
        cf = CategoryForm()
        context = {}
        context['form'] = cf
        return render(request, 'administrator/category_create.html', context)
    elif request.method == "POST":
        cf = CategoryForm(request.POST)
        if cf.is_valid():
            name = cf.cleaned_data['name']
            description = cf.cleaned_data['description']
            Category.objects.get_or_create(
                name=name,
                defaults={
                    'description': description
                }
            )

            return redirect('admin_category_list')
        return render(request, 'administrator/category_create.html', {'form': cf})
        

@login_required
def category_list(request):
    return render(request, 'administrator/category_index.html', {'data': Category.objects.all()})
