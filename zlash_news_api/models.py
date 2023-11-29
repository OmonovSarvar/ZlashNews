from django.db import models
from django.db.models.functions import datetime


class NewsModel(models.Model):
    # This model for News
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=700)
    url = models.CharField(max_length=200)
    day = models.CharField(max_length=11)

    def __str__(self):
        return f"New message from {self.title}"


