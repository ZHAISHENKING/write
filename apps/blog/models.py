from django.db import models
from django.conf import settings
from User.models import Ouser
# Create your models here.


# tags
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=20)
    desc = models.TextField('描述', max_length=240, default=settings.SITE_DESCRIPTION)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


# category
class Category(models.Model):
    name = models.CharField('文章分类', max_length=20)
    desc = models.TextField('描述', max_length=240, default=settings.SITE_DESCRIPTION)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


# article
class Article(models.Model):
    title = models.CharField('文章标题',max_length=150)
    content = models.TextField('文章内容')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    views = models.IntegerField('阅览量', default=0)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, verbose_name='文章分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
