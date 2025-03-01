from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import PermissionDenied, NotAuthenticated

from posts.models import Post, Group
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)


User = get_user_model()


class AuthorPermissionMixin:
    def perform_update(self, serializer):
        if not self.request.user.is_authenticated:
            raise NotAuthenticated('Пользователь не авторизован.')
        if serializer.instance.author.username != self.request.user.username:
            raise PermissionDenied('Изменение чужого контента запрещено.')
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        if not self.request.user.is_authenticated:
            raise NotAuthenticated('Пользователь не авторизован.')
        if instance.author.username != self.request.user.username:
            raise PermissionDenied('Удаление чужого контента запрещено.')
        return super().perform_destroy(instance)


class PostViewSet(AuthorPermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']


class CommentViewSet(AuthorPermissionMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'post']
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return self.request.user.subscriptions.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
