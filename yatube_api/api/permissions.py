from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class AuthorOrSafeMethodsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.author.username != request.user.username:
            raise PermissionDenied('Изменение чужого контента запрещено.')
        return True
