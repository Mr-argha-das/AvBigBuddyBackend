from django.db import models

class Banners(models.Model):
    image_path = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title