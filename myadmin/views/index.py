#! -*- coding: UTF-8 -*-
#@Time : 2022/2/3 18:15
#@Author : 中国
#@File : index.py
#@Software : PyCharm
from django.http import HttpResponse


def index(request):
    #接收到前端的处理逻辑，返回”欢迎来到点餐系统后台！“
    return HttpResponse("欢迎来到点餐系统后台！")