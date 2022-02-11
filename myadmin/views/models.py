#! -*- coding: UTF-8 -*-
# @Time : 2022/2/8 17:06
# @Author : 中国
# @File : models.py
# @Software : PyCharm


# 员工账号信息模型
from datetime import datetime

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)   # 员工账号
    nickname = models.CharField(max_length=50)   # 昵称
    password_hash = models.CharField(max_length=100) # 密码
    password_salt = models.CharField(max_length=50) # 密码干扰值
    status = models.IntegerField(default=1) # 状态：1正常/2禁用/9删除
    create_at =models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now) # 修改时间

# toDict()方法：将User表中的数据以字典的形式返回，后面做增删改查操作会经常用到该方法
    def toDict(self):
        return {'id':self.id, 'username':self.username, 'nickname':self.nickname, 'password_hash':self.password_hash, 'password_salt':self.password_salt, 'status': self.status, 'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'), 'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

# 如过不指定表名，Django默认创建的数据库表为"myapp_user",Meta类将表名指定为'user'
    class Meta:
        db_table = 'user'  # 更改表名