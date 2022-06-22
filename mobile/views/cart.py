#! -*- coding: UTF-8 -*-
# @Time : 2022/6/8 9:24
# @Author : 中国
# @File : cart.py
# @Software : PyCharm



# 购物车管理
from django.http import JsonResponse

from myadmin.models import Product


def add(request):
    '''添加购物车'''
    # 尝试从session中获取名字为cartlist的购物车信息，若没有返回{}
    cartlist = request.session.get("cartlist", {})
    # 获取要购买的菜品信息
    pid = request.GET.get("pid", None)
    if pid is not None:
        product = Product.objects.get(id=pid).toDict()
        product['num'] = 1 # 初始化当前菜品的购买量

        # 判断当前购物车中是否存在要放进购物车的菜品
        if pid in cartlist:
            cartlist[pid]['num'] += product['num']
        else:
            cartlist[pid] = product # 放进购物车

        #将cartlist购物车信息放入到session中
        request.session['cartlist'] = cartlist

        # 响应json格式的购物车数据
    return JsonResponse({'cartlist': cartlist})


def clear(request):
    '''清空购物车操作'''
    request.session['cartlist'] = {}
    return JsonResponse({'cartlist': {}})
#
# def delete(request):
#     '''删除购物车中的商品'''
#     cartlist = request.session['cartlist']
#     pid = request.GET.get("pid", None)
#     del cartlist[pid]
#     request.session['cartlist'] = cartlist
#     # 响应json格式的购物车信息
#     return JsonResponse({'cartlist': cartlist})


# def change(request):
#     '''购物车信息修改'''
#     cartlist = request.session['cartlist']
#     shopid = request.GET.get("pid", 0)
#     num = int(request.GET.get('num', 1))
#     if num < 1:
#         num = 1
#     cartlist[shopid]['num'] = num
#     request.session['cartlist'] = cartlist
#     #响应json格式的购物车信息
#     return JsonResponse({'cartlist': cartlist})