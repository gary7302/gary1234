from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
def spanishhome(request):
    category=SpanishCategory.objects.all()
    return render(request,'spanish-store/index.html',{'category':category})