from django.db import models
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    published_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    published = models.BooleanField(default=False)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    tagline = models.CharField(max_length=250)
    body = RichTextField()
    header_image = models.ImageField()

    def __str__(self):
        return self.title
