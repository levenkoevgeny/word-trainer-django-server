from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MyUser, Dictionary, Word


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        depth = 2


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class DictionarySerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Dictionary
        fields = '__all__'


