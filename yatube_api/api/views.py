# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from posts.models import Group, Post, Follow
from rest_framework import viewsets
# from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.select_related('author')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    #def get_queryset(self):
        #follow = get_object_or_404(Follow, id=self.kwargs.get('user_id'))
        # filter_backends = (filters.SearchFilter)
        # search_fields = ('name',)
        #return follow.select_related('user')
        
    #def perform_create(self, serializer):
        #follow = get_object_or_404(Follow, id=self.kwargs.get('user_id'))
        #serializer.save(user=self.request.user, user=follow)
