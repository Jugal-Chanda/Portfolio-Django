from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200,blank=False)
    post = models.TextField(blank=False)

    def __str__(self):
        return self.title
