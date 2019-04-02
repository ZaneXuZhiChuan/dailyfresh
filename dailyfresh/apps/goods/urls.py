# 三方
from django.conf.urls import url
# 自定义
from apps.goods import views

urlpatterns = [
    url(r'^$', views.index, name='index')  # 首页
]
