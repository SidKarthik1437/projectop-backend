from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import Prob

User = get_user_model()


class ProbSerializer(ModelSerializer):
    class Meta:
        model = Prob
        fields = '__all__'


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'name', 'email', 'phone', 'password')
