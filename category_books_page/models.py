from django.db import models

# Create your models here.
class BookProducts(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    summary = models.TextField(default='The summary is shown')