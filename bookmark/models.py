from django.db import models
from django.urls import reverse

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)
    url = models.URLField()
    contents = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Site name : " +self.site_name+", URL : " +self.url


    class Meta:
        ordering = ['site_name']