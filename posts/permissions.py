from rest_framework.permissions import BasePermission


class OwnerOrRead(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method == "GET":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or obj.author_name == request.user:
            return True
        return False
