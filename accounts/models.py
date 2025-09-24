from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username



class Profile(models.Model):
    """
    This model is for user's profile
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, default='lorem ipsum')
    phone_number = models.CharField(max_length=15, default='123456789')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
