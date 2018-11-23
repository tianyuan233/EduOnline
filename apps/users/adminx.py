#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2018/11/23
@file: adminx.py

"""
import xadmin
from users.models import EmailVerifyRecord, Banner

# X admin的全局配置信息设置
from xadmin import views


class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "后台管理"
    site_footer = "tianyuan233"


class EmailVerifyRecordAdmin(object):
    """
    list_display: 后台列出的字段
    search_fields: 搜索框及支持搜索的字段
    list_filter: 添加过滤器
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 将管理器与model进行注册关联
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

# 将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)
