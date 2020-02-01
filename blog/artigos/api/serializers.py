from rest_framework.serializers import ModelSerializer
from artigos.models import Artigo

class ArtigosSerializer(ModelSerializer):
    class Meta:
        model = Artigo
        fields = ['id', 'title', 'content', 'author', 'comments', 'images', 'created', 'modified', 'status']

        