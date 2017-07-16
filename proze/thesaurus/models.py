from django.contrib.postgres import fields as postgres_fields
from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)
    syllable_count = models.PositiveIntegerField()
    syllables = postgres_fields.ArrayField(
        models.CharField(max_length=255, blank=True)
    )

    def __str__(self):
        return self.word
