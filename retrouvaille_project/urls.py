"""
URL configuration for retrouvaille_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from forms_app.views import contact_view, register_account
from blog.views import blog_post_editor
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path("admin/", admin.site.urls),
   
    
    #  path("", HomeTemplateView.as_view(), name="homepage"),
    path('', include('core.urls')),
   
    path("contact-us/", contact_view, name = "contact_page"),
    path("blog-post-editor/", blog_post_editor, name="post-editor"), 
    path("accounts/login/", include("django.contrib.auth.urls")),
    path("accounts/logout/", include("django.contrib.auth.urls")),
    path("accounts/new/", register_account, name="register-account"),
    path("", include("cal.urls")),
  
    path("publicaties/", include("publicaties.urls")),
 
    path("publicaties/auhtor-detail", include("publicaties.urls")),
    
  
    
        
    ]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  





