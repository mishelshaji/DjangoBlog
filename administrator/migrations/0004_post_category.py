# Generated by Django 3.1.2 on 2020-12-18 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_auto_20201216_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrator.category'),
            preserve_default=False,
        ),
    ]