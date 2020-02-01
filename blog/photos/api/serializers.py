from rest_framework.serializers import ModelSerializer
from photos.models import Photo

class PhotosSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'img']
        
        