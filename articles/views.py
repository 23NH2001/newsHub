from .models import Article
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articlesListPage.html"
    
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name="articleDetailPage.html"
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields=("title","body")
    template_name="articleUpdatePage.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name="articleDeletePage.html"
    success_url = reverse_lazy("articles_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
        
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    fields = ("title","body")
    template_name="articleCreatePage.html"
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    