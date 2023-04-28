# User
# Token
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
