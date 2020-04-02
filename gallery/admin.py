from django.contrib import admin
from .models import Gallery #注册流程

# Register your models here.
admin.site.register(Gallery) #注册流程

# 还需要将文字等数据迁移到数据库里:
# python manage.py makemigrations
# python manage.py migrate

#python manage.py createsuperuser
#创建一个管理员 才能去网页进行管理
#haotian
#django123