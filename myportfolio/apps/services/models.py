from django.db import models
from django.core.urlresolvers import reverse # For update and create views

# Create your models here.
class Service(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
