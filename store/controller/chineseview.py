from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
def chinesehome(request):
    category=ChineseCategory.objects.all()
    return render(request,'chinese-store/index.html',{'category':category})