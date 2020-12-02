from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Book(models.Model):
    CATEGORY = (
        ('science', 'Science'),
        ('tech', 'Technology'),
        ('sports', 'Sports'),
    )

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Book Name',
        validators=[
            MinLengthValidator(3)
        ]
    )

    author = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Author'
    )

    published_on = models.DateField(
        blank=False,
        null=False,
        verbose_name='Published On'
    )

    price = models.IntegerField(
        default=0,
        verbose_name='Price',
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )
