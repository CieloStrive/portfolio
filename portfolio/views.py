#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    gallerys = Gallery.objects
    return render(request,'home.html', {'gallerys':gallerys }) #用字典形式传递变量

