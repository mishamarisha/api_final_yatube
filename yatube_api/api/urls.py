from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


API_VERSION_1 = 'v1'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='v1-posts')
router.register('groups', GroupViewSet, basename='v1-groups')
router.register('follow', FollowViewSet, basename='v1-follows')

post_comments_router = DefaultRouter()
post_comments_router.register(
    'comments', CommentViewSet, basename='v1-post-comments')

urlpatterns = [
    path(f'{API_VERSION_1}/', include(router.urls)),
    path(
        f'{API_VERSION_1}/posts/<int:post_id>/',
        include(post_comments_router.urls)),
    path(f'{API_VERSION_1}/', include('djoser.urls.jwt')),
]
