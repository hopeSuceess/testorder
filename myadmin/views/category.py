#! -*- coding: UTF-8 -*-
# @Time : 2022/3/18 16:11
# @Author : 中国
# @File : category.py
# @Software : PyCharm

# 菜品分类信息
from datetime import datetime

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from myadmin.models import Category, Shop


def index(request,pIndex=1):
    '''浏览信息'''
    smod = Category.objects
    mywhere = []
    list = smod.filter(status__lt=9)

    # 获取、判断并封装keyword键搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        list = list.filter(name__contains=kw)
        mywhere.append('keyword=' + kw)
    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        list = list.filter(status=status)
        mywhere.append('keyword=' + status)

    list = list.order_by("id") # 对id排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 10) #以10条每页创建分页对象
    maxpages = page.num_pages # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) # 当前页数据
    plist = page.page_range # 页码数列表

    # 遍历信息，并获得对应的商铺名称，以shopname名封装
    for vo in list2:
        sob = Shop.objects.get(id=vo.shop_id)
        vo.shopname = sob.name
    # 封装信息加载模板输出
    context = {"categorylist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/category/index.html", context=context)


def loadCategoy(request,sid):
    clist = Category.objects.filter(status__lt=9,shop_id=sid).values("id","name")
    # 返回QuerySet对象，使用list强转成对应的菜品分类列表信息
    return JsonResponse({'data': list(clist)})


def add(request):
    '''加载添加页面'''
    slist = Shop.objects.values("id", "name")
    context = {"shoplist":slist}
    return render(request, "myadmin/category/add.html",context)


def insert(request):
    ''' 执行表单添加 '''


    try:
        cod = Category()
        cod.shop_id = request.POST['shop_id']

        categoryName = request.POST.get('name', None)
        if categoryName:
            cod.name = categoryName
        else:
            context = {"info": "菜品分类不能为空"}
            return render(request, "myadmin/info.html", context)

        cod.status = 1
        cod.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cod.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cod.save()
        context = {"info": "新增成功!"}
    except Exception as e:
        print(e)
        context = {"info": "新增失败！"}
    return render(request, "myadmin/info.html", context)


def delete(request,sid):
    dataDel = Category.objects.get(id=sid)
    del dataDel
    context = {"info": "删除成功！"}
    return render(request,"myadmin/info.html",context)


def edit(request,sid):
    category = Category.objects.get(id=sid)
    slist = Shop.objects.values("id", "name")
    context = {"shoplist": slist, "category": category}
    return render(request, "myadmin/category/edit.html",context)


def update(request,sid):
    category = Category.objects.get(id = sid)
    category.shop_id = request.POST['shop_id']
    category.name = request.POST['name']
    category.status = request.POST['status']
    category.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category.save()
    context = {"info": "修改成功！"}
    return render(request, "myadmin/info.html", context)