""" this is my model  """
import os
from django.db import models
from django.db.models import Q
from tag.models import Tag


def get_filename_ext(file_path):
    """ this function for get image name and extention """
    base_name = os.path.basename(file_path)
    ext = os.path.splitext(base_name)
    return ext


def image_name(instance, filename):
    """ return uniqe file name for save in database """
    ext = get_filename_ext(filename)
    final_name = f"{instance.title}-{instance.id}{ext}"
    return f"media/Pictuer/{instance.title}/{final_name}"


class PostManger(models.Manager):

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        return self.get_queryset().filter(lookup).distinct()


class Post(models.Model):
    """ resposible for my post  """
    date = models.DateField(verbose_name='تاریخ')
    time = models.TimeField(auto_now=False, verbose_name='زمان')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(blank=False, unique=True, verbose_name='عنوان url')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=image_name, null=True, blank=True, verbose_name='عکس')

    PostTag = models.ManyToManyField(Tag, blank=True)
    objects = PostManger()

    class Meta():
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        """ this function return header of post as name of the post at admin page """
        return self.title
