# Generated by Django 3.2.11 on 2022-02-03 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20220203_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='author_name_kz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='author_name_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='body_text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_text_kz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_kz',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=20, null=True),
        ),
    ]