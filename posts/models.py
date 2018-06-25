from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
# Create your models here.

def upload_location(instance,filename) :
    return "%s/%s" %(instance.id,filename)


class PostManager(models.Manager) :
    def active(self,*args,**kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class Post(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, default=1)
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True,blank=True,width_field="width_field",height_field="height_field")
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.slug})
        # return "post/%s/" %(self.id)

    class Meta:
        ordering = ["-timestamp","updated"]

class Postingan(models.Model):
    isi = models.CharField(max_length=120)

    def __str__(self):
        return self.isi


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None :
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists :
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

# def pre_save_post_receiver(sender,instance,*args,**kwargs):
#    if not instance.slug :
#        instance.slug = create_slug(instance)
#
#
# pre_save.connect(pre_save_post_receiver,sender=Post)

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)