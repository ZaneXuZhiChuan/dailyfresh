# 内置模块
import re

# 三方模块
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

# 内置模块
from user.models import User


# Create your views here.
def register(request):
    return render(request, 'register.html')


# 注册处理
def register_handle(request):
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 数据校验
    if not all([username, password, email]):
        return render(request, 'register.html', {'errmsg': '数据不完整'})

    # 校验邮箱
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'register.html', {'errmsg': '请同意协议'})

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # 用户不存在
        user = None

    if user:
        return render(request, 'register.html', {'errmsg': '用户名已经存在'})

    user = User.objects.create_user(username, email, password)
    # 默认创建新用户时候，is_active 值为1,标记为激活状态，手动更改状态
    user.is_active = 0
    user.save()
    print('8'*80)
    # return render(request, 'index.html')
    return redirect(reverse('goods:index'))
