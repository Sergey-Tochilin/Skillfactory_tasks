"""
URL configuration for News_Portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from news_p import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsListViewset)
router.register(r'user', views.UserViewset)
router.register(r'author', views.AuthorViewset)
router.register(r'category', views.CategoryViewset)
router.register(r'articles', views.ArticlesListViewset)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('news/', include('news_p.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),

]
