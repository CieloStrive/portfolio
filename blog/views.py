from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog_page(request):
    blogs = Blog.objects
    return render(request,'blog.html', {'blogs':blogs} )

#写好view去最根目录里写url