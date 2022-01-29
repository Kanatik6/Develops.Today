from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet

router = SimpleRouter()
router.register("post", PostViewSet)
router.register("comment", CommentViewSet, basename="comment")

urlpatterns = []
urlpatterns += router.urls
