# Generated by Django 3.2.11 on 2022-02-03 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220203_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_name_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author_name_kz',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author_name_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_text_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_text_kz',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_text_ru',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_kz',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ru',
        ),
    ]