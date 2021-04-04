import random

from django.db import models
from django.conf import settings
from django.utils.text import slugify


def upload_location(self, instance, **kwargs):
    return 'articles/{}.jpg'.format(self.slug)


class Article(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    body = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to=upload_location, null=True)

    category = models.CharField(
        max_length=255, blank=True, default='Uncategorised')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    slug = models.SlugField(max_length=255, blank=True, unique=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                '{}-{}'.format(self.title, random.randint(10, 99)))
        super(Article, self).save(*args, **kwargs)
