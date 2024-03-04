from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'type', 'rating')
    list_filter = ('title', 'date', 'type', 'rating', )
    search_fields = ('title', 'category__name', 'author__user__username')#через поле автора обращаюсь к юзеру и уже к имени

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('subscribers',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)