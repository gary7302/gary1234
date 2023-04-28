from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Orderitems)
admin.site.register(Profile)
admin.site.register(CancerType)
admin.site.register(ChineseCategory)
admin.site.register(HindiCategory)
admin.site.register(SpanishCategory)
admin.site.register(Comment)
admin.site.register(SpanishComment)
admin.site.register(ChinaComment)
admin.site.register(HindiComment)
admin.site.register(Item)