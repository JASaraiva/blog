from rest_framework.serializers import ModelSerializer
from users.models import User

class UserSerialize(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'user', 'password', 'cellphone', 'email', 'role', 'status']
        
        