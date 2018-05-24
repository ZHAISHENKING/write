# templatetags/blog_tags.py

from django import template
from ..models import *
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def get_artcile_count():
    return Article.objects.count()


@register.simple_tag
def get_cate_count():
    return Category.objects.count()


@register.simple_tag
def get_tag_count():
    return Tag.objects.count()


@register.simple_tag
def my_highlight(text, q):
    '''自定义标题搜索词高亮函数'''
    try:
        r = text.replace(q, '<span class="highlighted">{}</span>'.format(q))
        return mark_safe(r)
    except:
        return text