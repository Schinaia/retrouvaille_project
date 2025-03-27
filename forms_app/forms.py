from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
       

 
class ContactForm(forms.Form):
    first_name = forms.CharField(label="Voornaam", min_length=3)
    last_name= forms.CharField(label="Achternaam", required=False)
    email = forms.EmailField()
    content = forms.CharField(
        label="Inhoud",
        widget=forms.Textarea(
            attrs={"placeholder": "Schrijf hier jouw bericht!", "class": "form-control"  }
        )
    )
    
    class Meta:
        model = User
        fields = ['first_name','last_name']
        labels = {
            'first_name': ("Voornaam"),
        }
        { 
            'last_name': ("Achternaam")
        }
        
       