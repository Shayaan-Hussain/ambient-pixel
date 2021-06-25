from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="imageFiles")
    user = models.CharField(max_length = 15)
    date = models.DateTimeField(auto_now_add=True)