#! -*- coding: UTF-8 -*-
#@Time : 2022/2/3 18:17
#@Author : 中国
#@File : index.py
#@Software : PyCharm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from myadmin.models import Category, Product, Shop


def index(request):
    # # 接收到前端的处理逻辑，返回”欢迎来到大堂点餐！“
    # return HttpResponse('欢迎来到手机移动端点餐页面！')

    '''移动端首页'''
    #获取并判断当前店铺信息
    shopinfo = request.session.get("shopinfo", None)
    if shopinfo is None:
        return redirect(reverse("mobile_shop")) # 重定向到店铺选择页
    # 获取当前店铺下的菜品类别和菜品信息
    clist = Category.objects.filter(shop_id=shopinfo['id'],status=1)
    productlist = dict()
    for vo in clist:
        plist = Product.objects.filter(category_id=vo.id, status=1)
        productlist[vo.id] = plist
        context = {'categorylist': clist, 'productlist': productlist.items(), 'cid': clist[0]}
    return render(request, "mobile/index.html", context)


def shop(request):
    '''呈现店铺选择页面'''
    context = {'shoplist': Shop.objects.filter(status=1)}
    return render(request, 'mobile/shop.html', context)


def selectShop(request):
    '''执行店铺选择'''
    # 获取店铺id号，通过店铺id号获取店铺信息
    sid = request.GET['sid']
    ob = Shop.objects.get(id=sid)
    # 将店铺信息放入到seession中
    request.session['shopinfo'] = ob.toDict()
    return redirect(reverse('mobile_index'))