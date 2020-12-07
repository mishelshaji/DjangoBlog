from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
def post_list(request):
    pass

@login_required
def post_create(request):
    if request.method == "GET":
        context = {}
        context['form'] = PostForm()
        return render(request, 'administrator/post_create.html', context)
    
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data saved")

        context = {}
        context['form'] = form
        return render(request, 'administrator/post_create.html', context)