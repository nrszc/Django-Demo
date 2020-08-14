from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # django默认包含的

    # 添加
    path('users/', include('users.urls')),
]