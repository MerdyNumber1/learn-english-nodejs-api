from rest_framework import serializers

from . import services
from .models import User
from .dto import UserDTO


class UserSerializer(serializers.ModelSerializer):
    registration_date = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'registration_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: UserDTO) -> User:
        return services.create_user(validated_data)