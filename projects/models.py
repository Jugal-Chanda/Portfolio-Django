from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200,blank=False)
    description = models.TextField(blank=False)
    link = models.URLField(blank=False)

    def __str__(self):
        return self.title
