from django.db import models


# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=512)


class Category(models.Model):
    category_name = models.CharField(max_length=512)


class Thumbnail(models.Model):
    name = models.CharField(max_length=512)
    thumbnail = models.ImageField(upload_to='media')


class Videos(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
