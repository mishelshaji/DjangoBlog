from django import forms
from django.forms import widgets
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '5'
                }
            ),
            'url': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class CategoryForm(forms.Form):
    name = forms.CharField(
        label='Category Name',
        min_length=3,
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        label='Description',
        min_length=10,
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '3'
            }
        )
    )