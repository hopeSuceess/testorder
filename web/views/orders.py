#! -*- coding: UTF-8 -*-
# @Time : 2022/7/19 17:27
# @Author : 中国
# @File : orders.py
# @Software : PyCharm
from datetime import datetime

from django.http import HttpResponse

from myadmin.models import Orders, Payment, OrderDetail


def insert(request):
    '''大堂执行订单添加操作'''
    print("try之前")
    try:
        print("try之后")
        # 执行订单信息添加操作
        od = Orders()
        od.shop_id = request.session['shopinfo']['id'] # 店铺id号
        od.member_id = 0 # 会员id
        od.user_id = request.session['webuser']['id'] #操作员id
        od.money = request.session['total_money']
        od.status = 1 # 订单状态：1进行中/2无效/3已完成
        od.payment_status = 2 # 支付状态：1未支付/2已支付/3已退款
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()
        print('Orders信息插入了没')

        #执行支付信息添加
        op = Payment()
        op.order_id = od.id #订单id号
        op.member_id = 0 #会员id号
        op.money = request.session['total_money'] # 支付款
        op.type = 2 # 付款方式：1.会员付款/2.收银收款
        op.bank = request.GET.get("bank", 3) # 收款银行渠道：1微信/2余额/3现金/4支付宝
        op.status = 2 # 支付状态：1.未支付/2.已支付/3.已退款
        op.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        # 执行订单详情的添加
        cartlist = request.session.get("cartlist", {}) # 获取购物车中的菜品信息
        # 遍历购物车中的菜品并添加到订单详情中
        for item in cartlist.values():
            ov = OrderDetail()
            ov.order_id = od.id # 订单id
            ov.product_id = item['id'] # 菜品id
            ov.product_name = item['name'] # 菜品名称
            ov.price = item['price'] # 单价
            ov.quantity = item['num'] # 数量
            ov.status = 1 # 状态：1正常/9删除
            ov.save()
        print(000)

        del request.session["cartlist"]
        del request.session["total_money"]
        print(111)
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return HttpResponse("N")