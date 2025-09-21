from django.db import models
from django.contrib.auth import get_user_model



class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    statut = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(255)

    def __str__(self):
        return self.name
