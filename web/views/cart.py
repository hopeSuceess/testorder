#! -*- coding: UTF-8 -*-
# @Time : 2022/7/15 21:33
# @Author : 中国
# @File : cart.py
# @Software : PyCharm
from django.shortcuts import redirect
from django.urls import reverse


def add(request,pid):
    '''添加购物车操作'''
    #从session中获取当前店铺中所有菜品信，并从中获取要放入购物车的菜品
    product = request.session['productlist'][pid]
    product['num'] = 1 # 初始化当前菜品的购买量
    # 尝试从session中获取名字为cartlist的购物车信息，若没有返回{}
    cartlist = request.session.get('cartlist', {})
    # 判断当前购物车中是否存在要放进购物车的菜品
    if pid in cartlist:
        cartlist[pid]['num'] += product['num'] #增加购买量
    else:
        cartlist[pid] = product # 放进购物车
    # 将cartlist购物车信息放入到session中
    request.session['cartlist'] = cartlist
    #跳转到点餐首页
    return redirect(reverse('web_index'))


def change(request):
    ''' 更改购物车信息操作 '''
    #尝试从session中获取名字为cartlist的购物车信息，若没有返回{}
    cartlist = request.session.get('cartlist', {})
    pid = request.GET.get("pid",0) # 获取要修改的菜品id
    m = int(request.GET.get('num',1)) #要修改的梳理
    if m < 1:
        m = 1
    cartlist[pid]['num'] = m #修改购物车中的数量
    # 将cartlist购物车信息放入到session中
    request.session['cartlist'] = cartlist
    # 跳转到点餐首页
    return redirect(reverse('web_index'))


def clear(request):
    del request.session['cartlist']


    return redirect(reverse('web_index'))


def delete(request,pid):
    cartlist = request.session.get('cartlist', {})
    del cartlist[pid]
    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))