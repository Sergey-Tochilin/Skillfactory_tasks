from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'all_news.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
