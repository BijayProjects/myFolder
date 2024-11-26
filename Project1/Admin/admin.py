from django.contrib import admin
from .models import Home,Services,About,Product,Feedbacks

# Register your models here.

@admin.register(Home)
class AdminHome(admin.ModelAdmin):
    list_display = ['id','title','paragraph']

@admin.register(Services)
class AdminServices(admin.ModelAdmin):
    list_display =['id','delivery','free_shipping', 'best_quality','customer_support']

@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display =['id','About_me' ]

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display =['id','product_name','price','description','image_product','VAT']

@admin.register(Feedbacks)
class AdminFeedbacks(admin.ModelAdmin):
    list_display =['id','userName','phoneNo','email','messages']