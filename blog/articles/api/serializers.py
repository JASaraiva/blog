from rest_framework.serializers import ModelSerializer
from articles.models import Article

class ArticlesSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'comments', 'images', 'created', 'modified', 'status']

        