from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .filters import PostFilter
from .forms import PostForm
from .models import Post


@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('profile')

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'all_news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

#Дженерик вывода 1 новости
class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

#Дженерик создания новости
class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news_p.add.post')
    template_name = 'news_add.html'
    form_class = PostForm

#дженерик изменения новости
class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news_p.change.post')
    template_name = 'news_add.html'
    form_class = PostForm

    #метод get_object используется вместо queryset, что бы получить информацию об объекте
    #который буду редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


#Дженерик удаления объекта
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


#Дженерик для поиска
class PostSearch(ListView):
    model = Post
    ordering = '-date'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET,  queryset)
        if self.request.GET:
            return self.filterset.qs
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

