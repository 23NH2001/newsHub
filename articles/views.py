from typing import Any
from .models import Article
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.views.generic.detail import SingleObjectMixin
# Create your views here.
class CommentGet(DetailView):
    model = Article
    template_name="articleDetailPage.html"
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "articleDetailPage.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse("articles_detail", kwargs={"pk": article.pk})

class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    
class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articlesListPage.html"
    
    
    
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
    