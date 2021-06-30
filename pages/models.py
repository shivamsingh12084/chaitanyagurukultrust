from django.db import models

# Create your models here.
class News(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='banners/', blank=True) # new


    def __str__(self):
        return self.title