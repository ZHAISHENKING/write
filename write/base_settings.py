# -*- coding: utf-8 -*-
# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 修改数据库为MySQL，并进行配置
        'NAME': 'write',
        'USER': 'root',
        'PASSWORD': 'Jiege..950417',
        'HOST': '47.104.229.81',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4', }
    }
}
 #邮箱配置
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = '18700790825@163.com'
EMAIL_HOST_PASSWORD = 'SHI930417'  # 这个不是邮箱密码，而是授权码
EMAIL_PORT = 465  # 由于阿里云的25端口打不开，所以必须使用SSL然后改用465端口
# 是否使用了SSL 或者TLS，为了用465端口，要使用这个
EMAIL_USE_SSL = True
# 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可

DEFAULT_FROM_EMAIL = 'houseGod <18700790825@163.com>'

# 网站默认设置和上下文信息
SITE_END_TITLE = 'HouseGod'
SITE_DESCRIPTION = '梦虽虚幻，却是自己的梦想；位虽低微，却是自己的岗位；屋虽简陋，却是自己的家；志虽渺小，却是自己的追求。'
SITE_KEYWORDS = 'python'