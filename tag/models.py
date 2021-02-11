from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.title
