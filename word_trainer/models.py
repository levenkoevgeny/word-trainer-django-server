from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, verbose_name="Last name", blank=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name="First name", blank=True, null=True)
    avatar = models.ImageField(verbose_name="Avatar", blank=True, null=True, upload_to="avatars")

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'


class Dictionary(models.Model):
    dictionary_name = models.CharField(max_length=255, verbose_name="Dictionary name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    date_created = models.DateTimeField(verbose_name="Date time created", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Date time updated", auto_now=True)
    logo = models.ImageField(verbose_name="Logo", blank=True, null=True, upload_to="avatars")
    visit_count = models.IntegerField(verbose_name="Visit count", default=0)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="Owner", blank=True, null=True)

    def __str__(self):
        return self.dictionary_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'


class Word(models.Model):
    word_rus = models.CharField(max_length=255, verbose_name="Word rus")
    word_eng = models.CharField(max_length=255, verbose_name="Word eng")
    date_created = models.DateTimeField(verbose_name="Date time created", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Date time updated", auto_now=True)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, verbose_name="Dictionary", related_name="words")

    def __str__(self):
        return self.word_rus + ' ' + self.word_eng

    class Meta:
        ordering = ('id',)
        verbose_name = 'Word'
        verbose_name_plural = 'Words'





