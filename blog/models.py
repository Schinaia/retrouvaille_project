from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField()
    
    def __str__(self):
        return self.title
  