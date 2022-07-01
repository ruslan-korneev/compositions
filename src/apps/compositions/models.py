from django.db import models


class Composition(models.Model):
    name = models.CharField(max_length=120, verbose_name="Title")
    description = models.TextField(verbose_name="Short Description")
    image = models.ImageField(verbose_name="Image")
