from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView
from webapp.models import User, Article, Comment, Rating
from django.urls import reverse_lazy
from webapp.forms import ArticleSearchForm, ArticleCreateForm, ArticleUpdateForm, CommentCreateForm, CommentUpdateForm
# Create your views here.


class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = ArticleSearchForm

    def get_queryset(self):
        article_title = self.request.GET.get('article_title')
        if not article_title:
            return Article.objects.all()
        else:
            return Article.objects.filter(title__contains=article_title)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class FavoritListView(DetailView):
    model = User
    template_name = 'user_favorit.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleCreateForm
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleUpdateForm
    success_url = reverse_lazy('article_list')

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentCreateForm
    success_url = reverse_lazy('article_list')

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    form_class = CommentUpdateForm
    success_url = reverse_lazy('article_list')