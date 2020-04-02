from django.db import models

# Create your models here.
#创建了model要注册在.admin里，app是一个程序，功能用model实现
class Gallery (models.Model): #搭建一个展示模块：gallery的框架
    description = models.CharField(default='Write intro. here', max_length=100 ) #属性，描述区域，字符区域

    image = models.ImageField(default='default.png' , upload_to='images/')
    # image需要一个url以及本地路径去存放，修改setting尾部
    # (时刻意识到自己是服务器端，在网站上上传的数据要存在服务器端，而不是直接在服务器端写出网页内容样式)

    title = models.CharField(default='Title', max_length=50 ) #添加一个title属性并用__str__方法使每个创造的Gallery object都显示这个名

    def __str__(self):
        return self.title

# 将model传递给主页home.html
# 靠的是views.py
# 如果有改变model就需要migrate