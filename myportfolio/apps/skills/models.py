from django.db import models
from django.core.urlresolvers import reverse # For update and create views
from apps.categories.models import Category

# Create your models here.
class Skill(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    score = models.IntegerField()
    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
