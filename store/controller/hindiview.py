from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError

def hindihome(request):
    category=HindiCategory.objects.all()
    return render(request,'hindi-store/index.html',{'category':category})

def hindidetails(request):
    return render(request,'hindi-store/details.html')

def hindicomment(request,id):
    eachProduct = HindiCategory.objects.get(id=id)

    form = HindiCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'hindi-store/coment.html', context)

def hindiaddcomment(request,id):
    if request.method == "POST":
        form = HindiCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = HindiCategory.objects.get(id=id)
            d = HindiComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('hindi')
    return HttpResponse('<h1>We are unable to add your comment</h1>')

def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            try:
                user=User.objects.create_user(username=username,password=form.cleaned_data['password1'])
                user.save()
                return redirect('/login')
            except IntegrityError:
                messages.warning(request,'This username has already taken. Choose different')
    context={'form':form}
    return render(request,'hindi-store/auth/register.html',context)