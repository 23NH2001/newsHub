from .models import Article
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.
class ArticlesListView(ListView):
    model = Article
    template_name = "articlesListPage.html"
    
class ArticleDetailView(DetailView):
    model = Article
    template_name="articleDetailPage.html"
    
class ArticleUpdateView(UpdateView):
    model = Article
    fields=("title","body")
    template_name="articleUpdatePage.html"
    
class ArticleDeleteView(DeleteView):
    model = Article
    template_name="articleDeletePage.html"
    success_url = reverse_lazy("articles_list")
    
class ArticleCreateView(CreateView):
    model = Article
    fields = ("title","body","author")
    template_name="articleCreatePage.html"