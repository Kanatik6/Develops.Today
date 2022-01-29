from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from posts.models import Comment
from posts.serializer import CommentSerializer


class SetCommentMixin:
    # я могу сделать просто через вьюшку комента, но думаю так по логике лучше, а crud уже в modelviewset'у сделать
    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticated],
        serializer_class=CommentSerializer,
    )
    def set_comment(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        validated_data = serializer.validated_data
        comment = Comment.objects.create(
            content=validated_data.get("content"), author_name=user, post=post
        )
        serializer = self.get_serializer_class()(comment)
        data = serializer.data

        return Response({"comment": data}, status=status.HTTP_201_CREATED)


class UpvotePostMixin:
    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticated],
    )
    def upvote(self, request, *args, **kwargs):
        post = self.get_object()
        post.upvote()
        post.save()

        serializer = self.get_serializer_class()(post)
        data = serializer.data
        return Response({"post": data}, status=status.HTTP_200_OK)
