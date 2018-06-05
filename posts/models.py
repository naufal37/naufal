from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

def upload_location(instance,filename) :
    return "%s/%s" %(instance.id,filename)


class Post(models.Model) :
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True,blank=True,width_field="width_field",height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"id": self.id})
        # return "post/%s/" %(self.id)

    class Meta:
        ordering = ["-timestamp","updated"]

class Postingan(models.Model):
    isi = models.CharField(max_length=120)

    def __str__(self):
        return self.isi

