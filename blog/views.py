from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, \
    CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets



from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CommentListCreateView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


