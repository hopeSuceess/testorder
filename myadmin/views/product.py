#! -*- coding: UTF-8 -*-
# @Time : 2022/5/24 19:52
# @Author : 中国
# @File : product.py
# @Software : PyCharm
import os
from datetime import time, datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from myadmin.models import Product, Shop, Category


def index(request,pIndex=1):
    '''浏览信息'''
    list = Product.objects.filter(status__lt=9)
    # smod = Product.objects
    # list = smod.filter(status__lt=9)
    mywhere = []

    # 获取、判断并封装keyword建搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询店铺名称中只要含有关键字就可以
        list = list.filter(Q(price__contains=kw) | Q(name__contains=kw))
        mywhere.append("keyword="+kw)

    list = list.order_by("id") # 对id排序
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

    for vo in list2:
        shopDetail = Shop.objects.get(id=vo.shop_id)
        vo.shopname = shopDetail.name
        categoryDetail = Category.objects.get(id=vo.category_id)
        vo.categoryname = categoryDetail.name

    # 封装信息加载模板输出
    context = {"productlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/product/index.html", context)

def categoryProduct(request,sid,pIndex=1):
    '''浏览信息'''
    list = Product.objects.filter(status__lt=9, category_id=sid)
    # smod = Product.objects
    # list = smod.filter(status__lt=9)
    mywhere = []

    # 获取、判断并封装keyword建搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询店铺名称中只要含有关键字就可以
        list = list.filter(Q(price__contains=kw) | Q(name__contains=kw))
        mywhere.append("keyword=" + kw)

    list = list.order_by("id")  # 对id排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 5)  # 以5条每页创建分页对象
    maxpages = page.num_pages  # 最大页数

    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    for vo in list2:
        shopDetail = Shop.objects.get(id=vo.shop_id)
        vo.shopname = shopDetail.name
        categoryDetail = Category.objects.get(id=vo.category_id)
        vo.categoryname = categoryDetail.name

    # 封装信息加载模板输出
    context = {"productlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/product/categoryProduct.html", context)

def add(request):
    """加载信息添加表单"""
    # 获取当前所以店铺
    slist = Shop.objects.values("id", "name")
    context = {"shoplist": slist}
    return render(request, "myadmin/product/add.html", context)

def insert(request):
    ''' 执行信息添加 '''
    try:
        # 图片的上传处理
        myfile = request.FILES.get("cover_pic", None)
        if not myfile:
            return HttpResponse("没有封面上传文件信息")
        cover_pic = str(time.strftime("%Y%m%d.%H%M%S"))+"."+myfile.name.split('.').pop()
        destination = open("./static/uploads/product/"+cover_pic,"wb+")
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()

        ob = Product()
        ob.shop_id = request.POST['shop_id']
        ob.category_id = request.POST['category_id']
        ob.name = request.POST['name']
        ob.price = request.POST['price']
        ob.cover_pic = cover_pic
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': '添加失败！'}
    return render(request, "myadmin/info.html", context)


def edit(request, sid):
    shopList = Shop.objects.values("id", "name")
    productList = Product.objects.get(id=sid)
    context = {'shoplist': shopList, 'product': productList}
    return render(request, "myadmin/product/edit.html", context)


def update(request,sid):
    try:
        # 获取原图片
        oldpicname = request.POST['oldpicname']
        # 图片的上传处理
        myfile = request.FILES.get("cover_pic", None)
        if not myfile:
            cover_pic = oldpicname
        else:
            cover_pic = str(time.strftime("%Y%m%d.%H%M%S"))+"."+myfile.name.split('.').pop()
            destination = open("./static/uploads/product/"+cover_pic, "wb+")
            for chunk in myfile.chunks():
                destination.write(chunk)
            destination.close()

        productList = Product.objects.get(id=sid)
        productList.shop_id = request.POST['shop_id']
        productList.category_id = request.POST['category_id']
        productList.name = request.POST['name']
        productList.price = request.POST['price']
        productList.cover_pic = request.POST['cover_pic']
        productList.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        productList.save()
        context = {'info': '修改成功！'}

        # 判断并删除老图片
        if myfile:
            os.remove("./static/uploads/product/"+oldpicname)
    except Exception as err:
        print(err)
        context = {'info': '添加失败！'}
        # 判断并删除新图片
        if myfile:
            os.remove("./static/uploads/product/"+cover_pic)
    return render(request, "myadmin/info.html", context)


def delete(request, sid):
    try:
        productDel = Product.objects.get(id=sid)
        productDel.status = 9
        productDel.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        productDel.save()
        context = {'info': '删除成功!'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败!'}
    return render(request, "myadmin/info.html",context)


