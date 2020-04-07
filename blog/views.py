from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.


def blog_page(request):
    blogs = Blog.objects
    return render(request,'blog.html', {'blogs':blogs} )

#view里要有对应url

def blog_article(request, blog_id):
    # 我们想根据model的object的id自动生成对应网页，即需要自动给传递不同object，
    # 需要from django.shortcuts import get_object_or_404

    blog = get_object_or_404(Blog, pk= blog_id) #获取到某个id的具体blog的object
    # blogs = Blog.objects
    return render(request,'blog_article.html', {'blog':blog})