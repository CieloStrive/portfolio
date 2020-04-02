from django.db import models

# Create your models here.
#创建了model要注册在.admin里，app是一个程序，功能用model实现
class Gallery (models.Model): #搭建一个展示模块：gallery的框架
    description = models.CharField( max_length=100 ) #属性，描述区域，字符区域

# 将model传递给主页home.html
# 靠的是views.py