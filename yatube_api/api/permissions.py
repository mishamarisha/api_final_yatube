from rest_framework import permissions


class AuthorOrSafeMethodsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (
            obj.author.username == request.user.username
            or request.method in permissions.SAFE_METHODS)
