from django.shortcuts import render
from .models import Book
from .forms import BookCreationForm

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'data':books})

def new_book(request):
    bcf = BookCreationForm()
    return render(request, 'book/create.html', {'form': bcf})