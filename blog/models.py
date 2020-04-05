from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(default='Article', max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.png', upload_to='images/')
    #默认图片存在media媒体根目录下
    text = models.TextField(default='Content')
    #创建model，去admin注册model

    def __str__(self):   #Blog object本身name
        return self.title
