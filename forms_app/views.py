from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic.base import TemplateView

from forms_app.forms import ContactForm, RegisterForm

# Create your views here.
# class HomeTemplateView(TemplateView):
#     template_name= "forms_app/home.html"
    
def register_account(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Niewe Account gemaakt</h1>")
    else:
        form = RegisterForm()         
    context = {"form": form}
    return render(request, "registration/register_account.html", context)
    
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(f"Naam: {form.cleaned_data['first_name']}")
            print(f"Achternaam: {form.cleaned_data['last_name']}")
            print(f"Email {form.cleaned_data['email']}")
            print(f"Inhoud: {form.cleaned_data['content']}")
            return HttpResponse("<h1>Bedankt dat u contact met ons opneemt!</h1>")
             
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "forms_app/contact_page.html", context)