from rest_framework import serializers
from django.contrib.auth.models import User

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'image', 'category',
                  'created_at', 'updated_at', 'author', 'slug']

    def get_username(self, article):
        return article.author.username
