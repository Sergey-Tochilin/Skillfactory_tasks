from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView

from .filters import PostFilter
from .forms import PostForm
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'all_news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

#Дженерик вывода 1 новости
class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

#Дженерик создания новости
class PostCreateView(CreateView):
    template_name = 'news_add.html'
    form_class = PostForm

#дженерик изменения новости
class PostUpdateView(UpdateView):
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
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

