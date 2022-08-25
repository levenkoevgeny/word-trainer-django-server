from django.contrib import admin
from .models import MyUser, Dictionary, Word

admin.site.register(MyUser)
admin.site.register(Dictionary)
admin.site.register(Word)
