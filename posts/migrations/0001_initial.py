# Generated by Django 3.2.11 on 2022-01-29 09:47

from django.conf import settings
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body_text', models.TextField()),
                ('link', models.URLField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('amount_of_upvotes', models.PositiveIntegerField(default=0)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_post', to='posts.post')),
            ],
        ),
    ]
