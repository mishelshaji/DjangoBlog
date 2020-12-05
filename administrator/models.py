from django.db import models
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = 'blog'

    id = models.BigAutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=150,
        verbose_name='Title',
        validators=[
            validators.MinLengthValidator(5)
        ]
    )

    description = models.TextField(
        verbose_name='Description',
        validators=[validators.MinLengthValidator(10)]
    )

    url = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='URL'
    )

    body = models.TextField(
        verbose_name='Post Content'
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Author'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )