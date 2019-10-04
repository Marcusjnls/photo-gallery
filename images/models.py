from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
    name= models.CharField(max_length=50)
    description = HTMLField()
    gallery_image = models.ImageField(upload_to='picha/', blank=True)
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location)

    @classmethod
    def all_images(self):

        return Image.objects.all()