from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import Client


class ClientSerializer(serializers.Serializer):
    class Meta:
        models = Client
        fields = ['id', 'code', 'is_activ']


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class AuthorizationValidateSerializer(UserValidateSerializer):
    pass


class RegistrationValidateSerializer(UserValidateSerializer):
    pass


    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise ValidationError('User already exists')
        except User.DoesNotExist:
            return username