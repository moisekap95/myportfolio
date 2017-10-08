from django.db import models
from django.core.urlresolvers import reverse # For update and create views
from apps.categories.models import Category

# Create your models here.
class Work(models.Model):

    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='+', on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    client = models.CharField(max_length=100)
    link = models.CharField(max_length=150)
    main_photo = models.ImageField(upload_to='img')
    gallery_photo_1 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_2 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_3 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_4 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_5 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_6 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_7 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_8 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_9 = models.ImageField(upload_to='img', null=True, blank=True)
    gallery_photo_10 = models.ImageField(upload_to='img', null=True, blank=True)


    def __str__(self):
        return self.title
