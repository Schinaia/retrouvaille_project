
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.shortcuts import render, redirect

from .models import Article, Author

from .forms import ArticleForm

# Create your views here
# def article_detail_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     context = { "article":article }
#     return render(request, "publicaties/detail_view.html", context)
  

# def publicaties_list (request):
#     articles = Article.objects.all()
#     authors = Author.objects.all()
#     context = {"articles":articles, "authors":authors}
#     return render(request, "publicaties/publicaties_list.html", context)

class AuthorDetailview(DetailView):
    model = Author
    
class ArticleListView(ListView):
    model = Article
    
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # Redirect to the list of articles
    else:
        form = ArticleForm()
    return render(request, 'article_list.html', {'form': form})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article _list.html', {'articles': articles})

   





  
 
  





    


    











# Create your views here.
