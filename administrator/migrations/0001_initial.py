# Generated by Django 3.1.2 on 2020-12-05 04:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Title')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Description')),
                ('url', models.CharField(max_length=255, unique=True, verbose_name='URL')),
                ('body', models.TextField(verbose_name='Post Content')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
