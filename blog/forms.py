from django.forms import ModelForm
from blog.models import BlogPost
from django import forms

class BlogPostModelForm(ModelForm):
 
    
    content=forms.CharField(
       widget=forms.Textarea(attrs={"placeholder":"Wat wil je met ons delen?"}),
       max_length= 4000, label="Eerst bericht")
  
                  
    class Meta:
        model = BlogPost
        fields = "__all__"
        labels = {
            'title': ('Titel'),
            'draft':('Voorlopige versie')
        }
     

        
