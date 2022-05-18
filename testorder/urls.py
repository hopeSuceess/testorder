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
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('myadmin/', include('myadmin.urls')), # 路由后缀是myadmin/  继续去myadmin.urls下寻找匹配的路由
    path('',include('web.urls')), # 跳转到web.urls下寻找匹配的路由
    path('mobile/',include('mobile.urls')), # 访问路径只有域名/IP+端口 跳转到mobile.urls下寻找匹配的路由

]
