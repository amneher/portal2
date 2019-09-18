from django.db import models

from django.contrib.auth.models import Employee


class Article(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = Employee()
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title()
    
    
class Comment(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = Employee()
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title()
    
    