#! -*- coding: UTF-8 -*-
# @Time : 2022/5/26 14:03
# @Author : 中国
# @File : member.py
# @Software : PyCharm
from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from myadmin.models import Member


def index(request, pIndex=1):
    list = Member.objects.filter(status__lt=9)
    mywhere = []

    kw = request.GET.get('keyword', None)
    if kw:
        list = list.filter(Q(nickname__contains=kw)| Q(mobile__contains=kw))
        mywhere.append("kwyword="+kw)

    status = request.GET.get('status', None)
    if status:
        list = list.filter(status=status)
        mywhere.append("status="+status)

    list = list.order_by('id') # 对id进行排序

    pIndex = int(pIndex)
    page = Paginator(list,5)     #以5条每页创建分页对象
    maxpages = page.num_pages   #最大页数

    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex<1:
        pIndex=1

    list2 = page.page(pIndex)   # 当前页数据
    plist= page.page_range      # 页码数列表

    context = {'memberlist': list2, 'maxpages': maxpages, 'pIndex':pIndex, 'plist':plist, 'mywhere': mywhere}

    return render(request, 'myadmin/member/index.html', context)


def delete(request,sid):
    ob = Member.objects.get(id=sid)
    ob.status = 9
    ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ob.save()
    context = {'info': '删除成功！'}
    return render(request, 'myadmin/info.html', context)