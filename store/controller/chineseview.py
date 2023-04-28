from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError


def chinesehome(request):
    category=ChineseCategory.objects.all()
    return render(request,'chinese-store/index.html',{'category':category})

def chinesegetpatch(request):
    return render(request,'chinese-store/getpatch.html')

def chineseusepatch(request):
    return render(request,'chinese-store/usepatch.html')

def chinesedetails(request):
    return render(request,'chinese-store/details.html')

def comment(request,id):
    eachProduct = ChineseCategory.objects.get(id=id)


    form = ChinaCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'chinese-store/coment.html',context)

def addComment(request,id):
    if request.method == "POST":
        form = ChinaCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = ChineseCategory.objects.get(id=id)
            c = ChinaComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            c.save()
            return redirect('chinese')
    return HttpResponse('<h1>We are uable to add your comment</h1>')

def register(request):
    form=CustomUserForm()
    if request.method == "POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            try:
                user=User.objects.create_user(username=username,password=form.cleaned_data['password1'])
                user.save()
                return redirect('/login')
            except IntegrityError:
                form.add_error('username','該用戶名已存在。嘗試使用其他用戶名')
    context={'form':form}
    return render(request,'chinese-store/auth/register.html',context)