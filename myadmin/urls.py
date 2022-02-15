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

from myadmin.views import index, user

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

]
