from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'register.html')


# 注册处理
def register_handle(request):
    pass
