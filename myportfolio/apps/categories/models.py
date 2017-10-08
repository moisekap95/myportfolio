from django.db import models
from django.core.urlresolvers import reverse # For update and create views

class Category(models.Model):
    MODELS = (
        ('W', 'Works'),
        ('S', 'Skills'),
    )
    name =  models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    model = models.CharField(max_length=50, choices=MODELS)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
