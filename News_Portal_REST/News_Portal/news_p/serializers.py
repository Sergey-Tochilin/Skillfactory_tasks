from .models import *
from rest_framework import serializers

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'type', 'date', 'title', 'text', 'author', 'category']

#class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'type', 'date', 'title', 'text', 'author', 'category']