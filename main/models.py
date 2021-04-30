from django.db import models
import datetime
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=280)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:listing_detail', args=[str(self.pk)])


class PostClick(models.Model):
    title = models.CharField(max_length=280)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title