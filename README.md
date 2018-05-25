#write
### 前言
此项目为Django开源学习项目
### 技术点
- 博客models设计
- 全局搜索
- xadmin后台管理
- 自定义模板标签TemplateTags
- 类视图继承Listview,DetialView用法
- 爱心点击动画及详情页时钟
- markdown及代码高亮
- 模板过滤器

### 食用方法
git上拉下来 由于涉及个人信息,我删除了一个base_settings.py文件
```
# -*- coding: utf-8 -*-
# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 修改数据库为MySQL，并进行配置
        'NAME': 'write',
        'USER': 'your_name',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4', }
    }
}


# 网站默认设置和上下文信息
SITE_END_TITLE = 'HouseGod'
SITE_DESCRIPTION = '梦虽虚幻，却是自己的梦想；位虽低微，却是自己的岗位；屋虽简陋，却是自己的家；志虽渺小，却是自己的追求。'
SITE_KEYWORDS = 'python'
```
配置完之后 创建虚拟环境并安装依赖
```
pip install -r reqirements.txt
```
再之后就是迁移数据库
```
python manage.py makemigrations
python manage.py migrate
python manage,py createsuperuser
```
如果懒的添数据可以
```
python manage.py loaddata blog.json
```
你会惊奇的发现多了分类 标签 等等
### 部署到服务器食用效果更佳
```
http://www.tendcode.com/article/set-up-django-with-nginx-and-gunicorn/
```