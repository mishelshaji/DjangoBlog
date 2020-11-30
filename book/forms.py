from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select
from .models import Book

class BookCreationForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Book Name'
                }
            ),
            'author': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'published_on': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'price': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }