from django.db import models
import random
import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Banners(models.Model):
    image_url = models.ImageField(upload_to=RandomFileName('image_url'), blank=True, null=True)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title