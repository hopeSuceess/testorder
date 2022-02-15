#! -*- coding: UTF-8 -*-
# @Time : 2022/2/8 17:41
# @Author : 中国
# @File : user.py
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from myadmin.views.models import User


def index(request,pIndex=1):
    """
    获取User数据表的信息，filter()是一个"过滤器"，把可迭代的变量中的值，挨个地传给函数进行处理。filter()可以传入参数。匹配与该参数相关的数据
    """
    umod = User.objects
    list = umod.filter(status__lt=9)

    mywhere = []   # 定义一个空列表

    # 获取、判断并封装keyword键关键字
    # keyword关键字对应index.html中的name="keyword"
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询员工账号或昵称中只要含有关键字的都可以
        # Q()函数的作用是模糊查询，在这里是只要正确输入账号或昵称一个关键字就能查询出来相关信息
        list = list.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        mywhere.append("keyword="+kw) # 将keyword=kw放入到mywhere列表中

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list,5) # 以5条每页创建分页对象
    maxpages = page.num_pages # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) # 当前页数据
    plist = page.page_range # 页码数列表


    # 将获取到的User信息放到字典中
    #将mywhere放到context字典中,待context将mywehere传到前端页面
    context = {'userlist': list2, 'plist':plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}

    '''
    将相关信息渲染到index.html中，并将User数据库的信息通过context传递过去
    '''
    return  render(request,'myadmin/user/index.html',context)

