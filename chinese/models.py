"""Defines the Character model for storing Chinese characters and statistics."""

from django.db import models


class Character(models.Model):
    """Represents a Chinese character with pinyin, translation, and usage statistics."""

    character = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    correct_count = models.PositiveIntegerField(default=0)
    incorrect_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        """Return the character as string representation."""
        return str(self.character)