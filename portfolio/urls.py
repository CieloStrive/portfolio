"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
import blog.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ),
    #path('blog/', blog.views.blog_page ),
    #参照上方注释里的推荐
    #按app分类管理
    #所有的导入和path都混合在这，不方便管理，推荐可以这样做：(给每个app一个url文件，去看blog里的url.py)用include按app分类
    #记得写blog+/，这样以后blog的网页以及后面继续生成的网页都去blog里的urls找。
    path('blog/', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
