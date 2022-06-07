#! -*- coding: UTF-8 -*-
#@Time : 2022/2/3 18:17
#@Author : 中国
#@File : index.py
#@Software : PyCharm
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from myadmin.models import Category, Product, Shop, Member


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


def register(request):
    '''加载注册/登录页面'''

    return render(request, "mobile/register.html")


def doRegister(request):
    '''执行注册/登录'''
    # 验证短信码
    verifycode = "1234" # request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info': '验证码错误'}
        return render(request, "mobile/register.html", context)

    try:
        #根据手机号码获取当前会员信息
        member = Member.objects.get(mobile=request.POST['mobile'])
    except Exception as err:
        # 此处可以执行当前会员注册(添加)
        ob = Member()
        ob.nickname = "顾客" #默认会员名称
        ob.avatar = "moren.png" # 默认头像
        ob.mobile = request.POST['mobile'] # 手机号码
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ob.save()
        member=ob
    # 检查当前会员状态
    if member.status == 1:
        # 将当前会员信息转换成字典格式并存放到seession中
        request.session['mobileuser'] = member.toDict()
        # 重定向到首页
        return redirect(reverse("mobile_index"))
    else:
        context = {"info": '此账号信息禁用'}
        return render(request, "mobile/register.html", context)
