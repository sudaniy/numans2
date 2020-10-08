from django.db import models
from django.utils import timezone

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Slider Galllery'

class About(models.Model):
    history = models.TextField()

    class Meta:
        verbose_name = 'About Us'

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Our Services'

class Gallery(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Projects Gallery'

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'News & Updates'

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Our Team'