#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2019/01/07
@file: urls.py

"""
from django.urls import path, re_path

from courses.views import CourseListView

app_name = "courses"
urlpatterns = [
    path('list/', CourseListView.as_view(), name="list"),
]