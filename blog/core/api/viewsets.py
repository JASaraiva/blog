from rest_framework.viewsets import ModelViewSet
from core.models import Core
from .serializers import CoreSerializer

class CoreViewSet(ModelViewSet):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer
