#! -*- coding: UTF-8 -*-
# @Time : 2022/2/21 20:46
# @Author : 中国
# @File : shopmiddleware.py
# @Software : PyCharm

import re

from django.shortcuts import redirect
from django.urls import reverse


class ShopMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):
        # 获取当前请求路径
        path = request.path
        print("url",path)

        # 判断管理后台是否登录
        # 定义后台不登录也可以直接访问的url列表
        urllist = ['/myadmin/login','/myadmin/logout','/myadmin/dologin', '/myadmin/verify']
        # 判断当前请求url地址是否是以/myadmin开头，并且不在urllist中，才做是否登陆判断
        if re.match(r"^/myadmin",path) and (path not in urllist):
            # 判断是否登录(在于session中没有adminuser)
            if "adminuser" not in request.session:
                # 重定向到登录页
                return redirect(reverse("myadmin_login"))

        # 判断大堂点餐是否登录
        urllist = ['login','dologin','verify']
        if re.match(r"^/web",path) and (path not in urllist):
            if "webuser" not in request.session:
                return redirect(reverse("web_login"))




        #判断H5移动会员端是否登录
        #定义移动端不登录也可以直接访问的url列表
        urllist1 = ['/mobile/register','/mobile/doregister']
        # 判断当前请求url地址是否是以/mobile开头，并且不在urllist中，才做是否登录判断
        if re.match(r'^/mobile', path) and (path not in urllist1):
            # 判断是否登录(在于session中没有mobileuser)
            if 'mobileuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("mobile_register"))

        response = self.get_response(request)
        return response

