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

from web.views import index, cart, orders

urlpatterns = [
    # path('admin/', admin.site.urls),
    # ''表示前端页面输入"xxx/web/"会跳到此处，index.index表示在web/views/index.py文件下的index函数处理此处的逻辑
    # name='web_index'：在前端代码中通过name值也能找到此处路由
    path('',index.index, name="index"),  # 前台大堂点餐首页

    # 前端登录退出的路由
    path('login', index.login, name = "web_login"), # 加载登陆表单
    path('dologin', index.dologin, name = "web_dologin"), # 执行登录
    path('verify', index.verify, name="web_verify"), #输出验证码





    # 为url路由添加请求前缀web/，凡是带此前缀的url地址必须登录后才能访问
    path("web/", include([
        path('', index.webIndex, name="web_index"),   #前台大堂点餐首页
        #购物车信息管理路由
        path('cart/add/<str:pid>', cart.add,name="web_cart_add"), #购物车新增
        path('cart/change', cart.change, name="web_cart_change"),  # 购物车更改
        path('cart/clear', cart.clear, name="web_cart_clear"), # 购物车清空
        path('cart/delete/<str:pid>', cart.delete, name="web_cart_delete"), # 购物车餐品删除

        path('delweb', index.delweb, name="web_delweb"),  # 退出大堂点餐系统

        # path('orders/insert', orders.insert,name='web_orders_insert'), #执行订单添加操作

    ]))
]
