from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=30,
        )
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")


