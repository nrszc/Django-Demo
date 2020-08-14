from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# urlpatterns是被django自动识别的路由列表变量
router = DefaultRouter()
# 申请单信息查询
router.register(r"apply", views.BookInfoViewSet)
urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^index/$', views.index),
    # url(r'^apply/$', views.BookInfoViewSet),
    path(r'', include(router.urls)),
]