from django.urls import reverse
from django.db import models
from django.core.files.storage import FileSystemStorage



# Create your models here.

    
class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name="Auteur"
        verbose_name_plural="Auteurs"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})
    
class Article (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name="articles")
    pdf_file = models.FileField(upload_to='pdffiles/', blank=True, null=True) 

    
    class Meta:
        verbose_name="Artikel"  
        verbose_name_plural="Artikels"

    
    def __str__(self):
        return self.title
    
    
      