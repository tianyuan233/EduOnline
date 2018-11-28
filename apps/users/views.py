from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
# 并集运算
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View

from users.forms import LoginForm
from users.models import UserProfile

#重写authenticate
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(
                Q(username=username) | Q(email=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self,
            # raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        redirect_url = request.GET.get('next', '')
        return render(request, "login.html", {
            "redirect_url": redirect_url
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            username = login_form.username
            password = login_form.password
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})

        else:
            return render(request, "login.html", {"login_form": login_form})



