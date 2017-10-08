from django.db import models
from django.core.urlresolvers import reverse # For update and create views

# Create your models here.
class Text(models.Model):

    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
