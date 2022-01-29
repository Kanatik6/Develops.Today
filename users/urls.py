from django.urls import path

from users.views import UserListView

urlpatterns = [path("users_list/", UserListView.as_view())]
