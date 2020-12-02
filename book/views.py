from django.shortcuts import redirect, render
from .models import Book
from .forms import BookCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'data':books})

def new_book(request):
    if request.method == "GET":
        bcf = BookCreationForm()
        return render(request, 'book/create.html', {'form': bcf})
    
    bcf = BookCreationForm(request.POST)
    if bcf.is_valid():
        bcf.save()
        messages.add_message(request, messages.SUCCESS, 'New Book Added')
        # messages.success(request, 'Data Saved')
        return redirect('book_home')
    return render(request, 'book/create.html', {'form': bcf})
