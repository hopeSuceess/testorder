#! -*- coding: UTF-8 -*-
# @Time : 2022/2/8 17:41
# @Author : 中国
# @File : user.py
from django.shortcuts import render

from myadmin.views.models import User


def index(request):
    """
    获取User数据表的信息，filter()是一个"过滤器"，把可迭代的变量中的值，挨个地传给函数进行处理。filter()可以传入参数。匹配于参数相关的数据
    """
    userlist = User.objects.filter()

    # 将获取到的User信息放到字典中
    context = {'userlist': userlist}

    '''
    将相关信息渲染到index.html中，并将User数据库的信息通过context传递过去
    '''
    return  render(request,'myadmin/index/index.html',context)

