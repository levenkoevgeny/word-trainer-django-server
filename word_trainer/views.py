from django.contrib.auth.models import User

from .models import MyUser, Dictionary, Word
from .serializers import MyUserSerializer, DictionarySerializer, WordSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.db.models import F
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action

from jose import jwt


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class DictionaryViewSet(viewsets.ModelViewSet):

    def list(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
            payload = jwt.decode(token, key=settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
        except jwt.JWTError:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            user_data = MyUser.objects.get(user_id=payload['user_id'])
        except MyUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if user_data.user.is_superuser:
            queryset = Dictionary.objects.all().order_by('-visit_count')
        else:
            queryset = Dictionary.objects.filter(owner=user_data).order_by('-visit_count')
        serializer = DictionarySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Dictionary.objects.all()
        dictionary = get_object_or_404(queryset, pk=pk)
        dictionary.visit_count = dictionary.visit_count + 1
        dictionary.save()
        serializer = DictionarySerializer(dictionary)
        return Response(serializer.data)

    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def common(self, request):
        queryset = Dictionary.objects.filter(owner__isnull=True).order_by('-visit_count')
        serializer = DictionarySerializer(queryset, many=True)
        return Response(serializer.data)


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        payload = jwt.decode(token, key=settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
    except jwt.JWTError:
        return Response(status=status.HTTP_403_FORBIDDEN)
    try:
        user_data = MyUser.objects.get(user_id=payload['user_id'])
        serializer = MyUserSerializer(user_data)
        return Response(serializer.data)
    except MyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@receiver(post_save, sender=User)
def user_post_save_handler(sender, instance, created, **kwargs):
    if isinstance(instance, User):
        if created:
            MyUser.objects.create(user=instance, last_name="Новый пользователь")