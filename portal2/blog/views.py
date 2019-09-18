from rest_framework import viewsets

from . import ArticleSerializer, CommentSerializer
from django.contrib.auth.models import Article, Comment


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer