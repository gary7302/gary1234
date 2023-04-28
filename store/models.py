
from django.db import models
from django.contrib.auth.models import User
import os
import datetime

# Create your models here.
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('uploads/',filename)
class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.CharField(max_length=200)
    big_description=models.TextField(max_length=500)
    price=models.IntegerField()
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s%s' %(self.category,self.name)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100,null=False)
    lname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    mobilenumber=models.IntegerField(null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state= models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField(null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=True)
    orderstatus=(
        ('pending','pending'),('Out For Delivery','Out For Delivery'),('completed','completed')
    )
    status=models.CharField(max_length=150,choices=orderstatus,default='pending')
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)

class Orderitems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id,self.order.tracking_no)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobilenumber = models.IntegerField(null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    product=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="comments")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

class CancerType(models.Model):
    type=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    description=models.TextField()

    def __str__(self):
        return self.type

def get_file_path_chinese(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('chinese_uploads/',filename)
class ChineseCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_chinese,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def get_file_path_hindi(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('hindi_uploads/',filename)
class HindiCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_hindi,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def get_file_path_spanish(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('spanish_uploads/',filename)
class SpanishCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_spanish,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class ChineseComment(models.Model):
#     product=models.ForeignKey(ChineseCategory,on_delete=models.CASCADE,related_name="chinesecomments")
#     commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
#     comment_body=models.TextField()
#     comment_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return "%s %s" %(self.product.name,self.commenter_name.username)

class ChinaComment(models.Model):
    product=models.ForeignKey(ChineseCategory,on_delete=models.CASCADE,related_name="chinacomments")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_chinese,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

class HindiComment(models.Model):
    product=models.ForeignKey(HindiCategory,on_delete=models.CASCADE,related_name="hindicomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_hindi,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

class SpanishComment(models.Model):
    product=models.ForeignKey(SpanishCategory,on_delete=models.CASCADE,related_name="spanishcomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_spanish,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_shopping(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('shopping_uploads/',filename)
class Item(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_shopping,null=True,blank=True)
    price=models.FloatField(null=False,blank=False)
    stock=models.IntegerField(null=False,blank=False)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name