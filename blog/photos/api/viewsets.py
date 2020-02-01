from rest_framework.viewsets import ModelViewSet
from photos.models import Photo
from .serializers import PhotosSerializer

class PhotosViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotosSerializer
