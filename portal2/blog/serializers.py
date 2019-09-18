from django.contrib.auth.models import Article, Comment

from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'date_created', 'content']
    
    
class CommentSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Comment
        fields = ['title', 'author', 'date_created', 'content']