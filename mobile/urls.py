"""testorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mobile.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    # ''表示前端页面直接输入域名或IP+端口会跳到此处，index.index表示在mobile/views/index.py文件下的index函数处理此处的逻辑
    # name='mobile_index'：在前端代码中通过name值也能找到此处路由
    path('',index.index, name="mobile_index")
]
