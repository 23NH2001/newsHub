from .views import ArticlesListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView
from django.urls import path

urlpatterns = [
    path("", ArticlesListView.as_view(), name="articles_list"),
    path("<int:pk>", ArticleDetailView.as_view(),name="articles_detail"),
    path("<int:pk>/edit", ArticleUpdateView.as_view(),name="articles_update"),
    path("<int:pk>/delete", ArticleDeleteView.as_view(),name="articles_delete"),
    path("new/", ArticleCreateView.as_view(),name="article_create"),
]
