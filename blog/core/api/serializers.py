from rest_framework.serializers import ModelSerializer
from core.models import Core

class CoreSerializer(ModelSerializer):
    class Meta:
        model = Core
        fields = ['title']
       