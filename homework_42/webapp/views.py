from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View, RedirectView
from webapp.models import User, Article, Comment, Rating
from django.urls import reverse_lazy
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'