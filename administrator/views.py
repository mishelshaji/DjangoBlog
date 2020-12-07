from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def post_list(request):
    pass

def post_create(request):
    if request.method == "GET":
        context = {}
        context['form'] = PostForm()
        return render(request, 'administrator/post_create.html', context)