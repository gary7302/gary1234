from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from .forms import *
from django.views.generic import View
from django.utils.translation import gettext as _
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.cache import never_cache
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.middleware import locale
from django.middleware.locale import LocaleMiddleware
from django.utils.decorators import method_decorator
# Create your views here.
def home(request):
    category=Category.objects.all()
    return render(request,'store/index.html',{'category':category})

# def type(request,slug):
#     if(Category.objects.filter(slug=slug)):
#         product=Product.objects.filter(category__slug=slug)
#         category_name=Category.objects.filter(slug=slug)
#         context={'product':product,'category':category_name}
#         return render(request,'store/products/index.html',context)
#     else:
#         messages.warning(request,'No such category found')
#         return redirect('home')

def comment(request,id):
    eachProduct = Category.objects.get(id=id)


    form = CommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'store/coment.html',context)

def addComment(request,id):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = Category.objects.get(id=id)
            c = Comment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                        comment_image=comment_image, created_at=datetime.now())
            c.save()
            return redirect('/')
    return HttpResponse('<h1>We are unable to add your comment</h1>')

def cancer(request,type):
    cancertype=CancerType.objects.filter(type=type)

    return render(request,'store/cancer/breast.html',{'cancer':cancertype})

def details(request):
    return render(request,'store/details.html')

def getpatch(request):
    return render(request,'store/getpatch.html')

def usepatch(request):
    return render(request,'store/usepatch.html')

def shopping(request):
    item=Item.objects.all()
    return render(request,'store/shopping.html',{'item':item})
