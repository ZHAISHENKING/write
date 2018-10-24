from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.text import slugify
from .models import Article, Tag, Category
from django.db.models.aggregates import Count
from markdown.extensions.toc import TocExtension  # 锚点的拓展
import markdown
from django.conf import settings

from haystack.generic_views import SearchView  # 导入搜索视图
from haystack.query import SearchQuerySet

from django.core import serializers
import time, datetime
from django.db.models import Q

# Create your views here.


class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article'
    paginate_by = 200
    paginate_orphans = 50


class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get_object(self):
        obj = super(DetailView, self).get_object()
        # 阅读量+1
        obj.increase_views()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        obj.content = md.convert(obj.content)
        obj.toc = md.toc
        return obj


class CategoryView(generic.ListView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'category'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'blog/categories.html'
    context_object_name = 'category'


class TagsView(generic.ListView):
    model = Tag
    template_name = 'blog/tags.html'
    context_object_name = 'tag'


class TagsDetailView(generic.DetailView):
    model = Tag
    template_name = 'blog/tagdetail.html'
    context_object_name = 'tags'


class ArchivesView(IndexView):
    template_name = 'blog/archives.html'


class AboutView(IndexView):
    template_name = 'blog/about.html'


class CommentView(IndexView):
    template_name = 'blog/comment.html'


# 重写搜索视图，可以增加一些额外的参数，且可以重新定义名称
class MySearchView(SearchView):
    context_object_name = 'search_list'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 0)
    queryset = SearchQuerySet().order_by('-views')

