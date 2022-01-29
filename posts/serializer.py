from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body_text",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]
        read_only_fields = ["author_name", "creation_date", "amount_of_upvotes"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author_name", "post", "content", "creation_date"]
        read_only_fields = ["author_name", "creation_date", "post"]
