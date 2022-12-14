# Generated by Django 4.1 on 2022-08-30 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dictionary_name', models.CharField(max_length=255, verbose_name='Dictionary name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date time created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date time updated')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='dictionary', verbose_name='Logo')),
                ('visit_count', models.IntegerField(default=0, verbose_name='Visit count')),
            ],
            options={
                'verbose_name': 'Dictionary',
                'verbose_name_plural': 'Dictionaries',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_rus', models.CharField(max_length=255, verbose_name='Word rus')),
                ('word_eng', models.CharField(max_length=255, verbose_name='Word eng')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date time created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date time updated')),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='word_trainer.dictionary', verbose_name='Dictionary')),
            ],
            options={
                'verbose_name': 'Word',
                'verbose_name_plural': 'Words',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last name')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First name')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'MyUser',
                'verbose_name_plural': 'MyUsers',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='dictionary',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='word_trainer.myuser', verbose_name='Owner'),
        ),
    ]
