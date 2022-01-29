from rest_framework.viewsets import generics

from django.contrib.auth import get_user_model

from users.serializer import UserSerializer

User = get_user_model()


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
