from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=20,
    )
    body_text = models.TextField()
    link = models.URLField()
    creation_date = models.DateField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts_author"
    )

    # без создания отдельной модели, без проверок на юзера и т.п. чисто по тз делаю
    def upvote(self):
        self.amount_of_upvotes += 1
        self.save()

    def __str__(self):
        return f"{self.authod_name}, - {self.title}"


class Comment(models.Model):
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_user"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments_post"
    )
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name}, - {self.post}"
