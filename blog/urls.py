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

from django.urls import path
from . import  views


urlpatterns = [
    path('', views.blog_page), #这里因为在最顶层urls里写了/blog都来这里查询。此处的空path已经是.../blog/了
    path('<int:blog_id>/', views.blog_article)
    # 对于完整博文网页的处理，根据model的隐藏属性id生成url
    # blog_id也会传递进views.blog_article，记得写在参数列表里
    # 在views里也处理一下
]
