from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=120)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

class Postingan(models.Model):
    isi = models.CharField(max_length=120)

    def __str__(self):
        return self.title
        return self.isi
