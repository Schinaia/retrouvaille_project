from django.shortcuts import render
from django.views.generic.base import TemplateView



# Create your views here.
# def homepage(request):
#     return render(request, 'core/homepage.html')
class HomeTemplateView(TemplateView):
    template_name= "core/home.html"
    
def programma(request):
    return render(request, "core/hetprogramma.html")
def contatto(request):
    return render(request, "core/contatto.html")
def uitdaging(request):
    return render(request, "core/deuitdaging.html")
def faq(request):
    return render (request, "core/faq.html")




