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

from myadmin.views import index, user, shop, category

urlpatterns = [
    # path('admin/', admin.site.urls),

    # ''表示前端页面输入"xxx/myadmin/"会跳到此处，index.index表示在myadmin/views/index.py文件下的index函数处理此处的逻辑
    # name='myadmin_index'：在前端代码中通过name值也能找到此处路由
    path('', index.index, name='myadmin_index'),
    
    
    #  员工账号信息管理
    # 'user'表示前端页面输入"xxx/myadmin/user"回跳到此处，user.index表示在myadmin/views/user.py文件下的index函数处理此处的逻辑
    # name="myadmin_user_index"：在前端代码中通过name值也能找到此处路由
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),  # 浏览信息,<int:pIndex>表示pIndex是int类型的参数
    path('user/add', user.add, name="myadmin_user_add"),  # 加载添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"), # 执行表单添加
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"), # 加载编辑页面
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # 执行编辑页面
    path('user/delete/<int:uid>',user.delete, name='myadmin_user_delete'), # 员工信息删除

    # 后台管理员路由
    path('login',index.login, name="myadmin_login"),
    path('dologin',index.dologin, name="myadmin_dologin"),
    path('logout', index.logout, name="myadmin_logout"),
    path('verify', index.verify, name="myadmin_verify"), #验证码

    # 店铺路由
    path('shop/<int:pIndex>', shop.index, name="myadmin_shop_index"),
    path('shop/add', shop.add, name="myadmin_shop_add"),
    path('shop/insert', shop.insert, name="myadmin_shop_insert"),
    path('shop/del/<int:sid>', shop.delete, name="myadmin_shop_del"),
    path('shop/edit/<int:sid>', shop.edit, name="myadmin_shop_edit"),
    path('shop/update/<int:sid>', shop.update, name="myadmin_shop_update"),


    # 菜品分类信息管理
    path('category/<int:pIndex>', category.index, name="myadmin_category_index"),
    path('category/load/<int:sid>', category.loadCategoy, name="myadmin_category_load"),
    path('category/add', category.add, name="myadmin_category_add"), # 添加表单
    path('category/insert',category.insert, name="myadmin_category_insert"), # 执行添加
    path('category/edit/<int:sid>', category.edit, name="myadmin_category_edit"), # 修改表单
    path('category/update/<int:sid>', category.update, name="myadmin_category_update"), # 执行修改
    path('category/delete/<int:sid>',category.delete, name="myadmin_category_delete"), # 删除










































]
