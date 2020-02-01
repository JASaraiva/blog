from django.contrib.auth.models import User
from users.api.serializers import UsersSerializer
from rest_framework.viewsets import ModelViewSet

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
   