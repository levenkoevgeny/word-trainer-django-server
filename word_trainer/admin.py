from django.contrib import admin
from .models import MyUser, Dictionary, Word
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(MyUser)
admin.site.register(Dictionary)
#admin.site.register(Word)

class WordResource(resources.ModelResource):

    class Meta:
        model = Word
        fields = ('id', 'dictionary', 'word_rus', 'word_eng')


class WordAdmin(ImportExportModelAdmin):
    resource_class = WordResource


admin.site.register(Word, WordAdmin)
