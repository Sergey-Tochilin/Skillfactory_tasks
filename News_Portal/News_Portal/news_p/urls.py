from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='news_detail'),
    path('create/', PostCreateView.as_view(), name='news_add'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='news_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='news_delete'),
    path('search/', PostSearch.as_view(), name='search')

]
