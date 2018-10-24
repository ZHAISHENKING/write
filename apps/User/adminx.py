import xadmin

from .models import Ouser
from xadmin import views


# 全局修改
class GlobalSettings(object):
    # 修改title
    site_title = '博客后台管理系统'
    # 修改footer
    site_footer = 'house god'
    # 收起菜单
    # menu_style = 'accordion'


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
