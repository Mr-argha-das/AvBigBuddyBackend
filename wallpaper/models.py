from django.db import models

class User(models.Model):
    en_login_id = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + ',' + self.email