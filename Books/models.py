from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    book_name = models.CharField(max_length=255, null=False, blank=True)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    book_genre = models.CharField(max_length=255, null=False, blank=True)
    book_rating = models.IntegerField(default=7)

    def __str__(self):
        return self.book_name