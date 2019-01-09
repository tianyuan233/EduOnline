#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2019/01/07
@file: urls.py

"""
from django.urls import path, re_path

from courses.views import CourseListView, CourseDetailView

app_name = "courses"
urlpatterns = [
    path('list/', CourseListView.as_view(), name="list"),
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="detail"),
]