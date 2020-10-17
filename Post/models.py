from django.db import models
import os


def get_filename_ext(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def image_name(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}-{instance.id}{ext}"
    return f"media/Pictuer/{instance.title}/{final_name}"


class Post(models.Model):
    """ resposible for my post  """
    date = models.DateField()
    time = models.TimeField(auto_now=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=image_name, null=True, blank=True)


    def __str__(self):
        """ this function return header of post as name of the post at admin page """
        return self.title
