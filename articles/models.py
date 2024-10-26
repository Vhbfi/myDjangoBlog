from django.db import models
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(default="",max_length=5000)
    slug = models.SlugField(default="",max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.title


    def snnipet(self):
        return self.body[:50] + " ..."