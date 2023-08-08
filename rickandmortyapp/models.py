from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=200)
    origin_name = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return self.name
