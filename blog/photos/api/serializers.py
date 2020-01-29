from rest_framework.serializers import ModelSerializer
from artigos.models import Artigo

class ArtigoSerializer(ModelSerializer):
    class Meta:
        model = Artigo
        fields = ['id', 'title', 'content', 'author', 'created', 'modificated']
        
        