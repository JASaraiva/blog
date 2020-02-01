from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from .serializers import CommentsSerializer

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
