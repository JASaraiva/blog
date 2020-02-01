from rest_framework.viewsets import ModelViewSet
from artigos.models import Artigo
from .serializers import ArtigosSerializer

class ArtigosViewSet(ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigosSerializer
