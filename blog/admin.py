from django.contrib import admin
from .models import Blog
# Register your models here.

admin.site.register(Blog)

#注册完去migrate
#这次将html创建在Blog里，view也在app里，这也是一种习惯