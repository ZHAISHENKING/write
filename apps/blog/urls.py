from django.contrib import admin
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
    url(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),  # 文章内容页
    url(r'^categories/$', CategoryView.as_view(), name='category'),
    url(r'^categories/(?P<pk>[\w+]+)/$', CategoryDetailView.as_view(), name='categories'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^tags/$', TagsView.as_view(), name='tags'),
    url(r'tags/(?P<pk>[\w+]+)/$',TagsDetailView.as_view(), name='tagsDetail'),
    url(r'^archives/$', ArchivesView.as_view(), name='archives'),
    url(r'^comments/$',CommentView.as_view(), name='comment'),
    url(r'^search/$', MySearchView.as_view(), name='search_view'),  # 全文搜索
]