from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Comment
from posts.serializer import PostSerializer, CommentSerializer
from posts.permissions import OwnerOrRead
from posts.mixins import SetCommentMixin, UpvotePostMixin


class PostViewSet(ModelViewSet, SetCommentMixin, UpvotePostMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        OwnerOrRead,
    ]

    def perform_create(self, serializer):
        print(self.request.user)
        return serializer.save(author_name=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        OwnerOrRead,
    ]
