# #! -*- coding: UTF-8 -*-
# # @Time : 2022/7/19 17:27
# # @Author : 中国
# # @File : orders.py
# # @Software : PyCharm
# from datetime import datetime
#
# from myadmin.models import Orders, Payment
#
#
# def insert(request):
#     '''大堂执行订单添加操作'''
#     try:
#         # 执行订单新型添加操作
#         od = Orders()
#         od.shop_id = request['shopinfo']['id'] # 店铺id号
#         od.member_id = 0 # 会员id
#         od.user_id = request.session['shopinfo']['id'] #操作员id
#         od.money = request.session['total_money']
#         od.status = 1 # 订单状态：1进行中/2无效/3已完成
#         od.payment_status = 2 # 支付状态：1未支付/2已支付/3已退款
#         od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         od.save()
#
#         #执行支付信息添加
#         op = Payment()
#         op.order_id = od.id #订单id号
#         op.member_id = 0 #会员id号