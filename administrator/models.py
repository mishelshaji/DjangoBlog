from django.db import models
from django.core import validators
# from django.contrib.auth.models import User
from accounts.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=20,
        verbose_name='Category Name',
        unique=True
    )

    description = models.TextField(
        verbose_name='Description',
        validators=[validators.MinLengthValidator(10)]
    )

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    def get_by_author(self):
        return super().get_queryset().filter(author_id=2)

class Post(models.Model):
    class Meta:
        db_table = 'blog'

    custom = PostManager()
    objects = models.Manager()

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

    featured_image = models.ImageField(
        verbose_name='Featured Image',
        upload_to = 'images/',
        blank = True
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

    category = models.ForeignKey(
        to=Category,
        default=1,
        on_delete=models.CASCADE
    )