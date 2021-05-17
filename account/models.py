from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Contributor(AbstractUser):
    GENDER_CHOICES = (
        ("M","Male"),
        ("F","Female"),
        ("U","Undisclosed"),
    )
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default="M")