from django.db import models
from django.contrib.auth.models import User


class Writer(models.Model):
    """
    User model for each write on the website, requires a writer image,
    an occupation and a user image
    """
    user = models.OneToOneField(User)
    occupation = models.CharField(max_length=100, blank=False)
    image = models.URLField(blank=False)