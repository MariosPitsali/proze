from django.contrib import admin

from thesaurus import models


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    pass
