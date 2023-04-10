from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
def hindihome(request):
    category=HindiCategory.objects.all()
    return render(request,'hindi-store/index.html',{'category':category})