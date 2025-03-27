from django.urls import path


from . import views
from core.views import HomeTemplateView




urlpatterns = [
    # path('', views.homepage, name="homepage"),
    path("", HomeTemplateView.as_view(), name="homepage"),
    
    path("programma/", views.programma, name="hetprogramma"),
    path("contatto/", views.contatto, name="contatto"),
    path("uitdaging/", views.uitdaging, name="deuitdaging"),
    path("faq/",views.faq, name="faq")
   

    
  
     
 ]
 