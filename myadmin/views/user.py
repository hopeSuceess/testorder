#! -*- coding: UTF-8 -*-
# @Time : 2022/2/8 17:41
# @Author : 中国
# @File : user.py
from django.core.paginator import Paginator
from django.shortcuts import render

from myadmin.views.models import User


def index(request,pIndex=1):
    """
    获取User数据表的信息，filter()是一个"过滤器"，把可迭代的变量中的值，挨个地传给函数进行处理。filter()可以传入参数。匹配与该参数相关的数据
    """
    userlist = User.objects.filter()



    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(userlist,5) # 以5条每页创建分页对象
    maxpages = page.num_pages # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) # 当前页数据
    plist = page.page_range # 页码数列表


    # 将获取到的User信息放到字典中
    context = {'userlist': list2, 'plist':plist, 'pIndex': pIndex, 'maxpages': maxpages}

    '''
    将相关信息渲染到index.html中，并将User数据库的信息通过context传递过去
    '''
    return  render(request,'myadmin/index/index.html',context)

