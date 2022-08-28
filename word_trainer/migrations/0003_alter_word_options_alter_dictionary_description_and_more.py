# Generated by Django 4.1 on 2022-08-28 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('word_trainer', '0002_dictionary_word'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('id',), 'verbose_name': 'Word', 'verbose_name_plural': 'Words'},
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='word',
            name='dictionary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='word_trainer.dictionary', verbose_name='Dictionary'),
        ),
    ]
