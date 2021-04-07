from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from settings.models import Settings


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('countries', 'sources', 'keywords')


class UserRegistrationSerializer(UserCreateSerializer):
    email = serializers.EmailField(required=True)