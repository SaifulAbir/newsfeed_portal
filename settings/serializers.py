from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from settings.models import Settings, Country, Source, Keyword


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name']


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']


class SettingsDetailSerializer(serializers.ModelSerializer):
    countries = CountrySerializer(many=True)
    sources = SourceSerializer(many=True)
    keywords = KeywordSerializer(many=True)
    user = UserSerializer(many=False)
    class Meta:
        model = Settings
        fields = '__all__'


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class UserRegistrationSerializer(UserCreateSerializer):
    email = serializers.EmailField(required=True)