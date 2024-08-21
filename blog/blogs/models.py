from django.db import models

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=50, unique=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)