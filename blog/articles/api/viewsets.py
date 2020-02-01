from rest_framework.viewsets import ModelViewSet
from articles.models import Article
from .serializers import ArticlesSerializer

class ArticlesViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
