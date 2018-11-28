#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@version:
@author: tianyuan233
@time: 2018/11/28
@file: forms.py

"""
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)