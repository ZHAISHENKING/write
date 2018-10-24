import xadmin

from .models import Article, Category, Tag


class TagAdmin(object):
    list_display = ['name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc']


class CategoryAdmin(object):
    list_display = ['name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc']


class ArticleAdmin(object):
    list_display = ['title', 'content', 'views', 'category', 'tags', 'user', 'slug']
    search_fields = ['title', 'content', 'views', 'category', 'tags', 'user', 'slug']
    list_filter = ['title', 'content', 'views', 'category', 'tags', 'user', 'slug', 'create_date']


xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Article,ArticleAdmin)
