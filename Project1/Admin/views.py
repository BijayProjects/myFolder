from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'main/dashboard.html')

class SigIn:
    def signin(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']

            
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'User Name does not exit!')
                return redirect('signin')

            aut_user = authenticate(username=username,password=password)
            if aut_user is not None and aut_user.is_superuser and aut_user.is_staff:
                login(request, aut_user)
                return redirect('dashboard')
            
            else:
                messages.error(request, "Invalid Password, Please try again!!")
                return redirect('signin')

            
        return render(request, 'main/login.html')

class SignUp:
    def signup(request):
        return render(request, 'main/register.html')
    
class SignOut:
    def signOut(request):
        logout(request)
        return redirect('signin')
    

def order_table(request):
    show_order = Order_Detail.objects.all()
    context = {
        'orders':show_order
    }
    return render(request, 'main/ordertables.html',context)

def headline(request):
    show_title = Home.objects.all()

    context = {
        'title':show_title
    }
    return render(request, 'main/headline.html',context)
def delete_headline(request,id):
    h_delete = Home.objects.get(id=id)
    h_delete.delete()
    messages.info(request, 'Delete Successfully')
    return redirect('headline')


def about_me(request):
    show_about = About.objects.all()
    context ={
        'about':show_about
    }
    return render(request, 'main/aboutme.html',context)

def add_products(request):
    if request.method == 'POST' and request.FILES:
        product_name =request.POST['product_name']
        products_price = request.POST['products_price']
        description = request.POST['description']
        product_images = request.FILES['product_image']
        vat = request.POST['vat']
        product= Product(product_name = product_name, price = products_price, description = description, image_product = product_images,VAT=vat)
        product.save()
        return redirect('view_products')

    return render(request, 'main/add_products.html')

def Product_delete(request,id):
    get_Product = Product.objects.get(id=id)
    get_Product.delete()
    messages.info(request, 'Products has been deleted Successfully')
    return redirect('view_products')


def view_products(request):
    show_product = Product.objects.all()
    context={
        'products':show_product
    }
    return render(request, 'main/view_products.html',context)

def Customer_Testimonial(request):
    testimonial =Feedbacks.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'main/Testimonal.html',context)

def Customer_Contact(request):
    testimonial =Feedbacks.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'main/customerContact.html',context)


class Add_pages:
    def add_headline(request):
        if request.method == "POST":
            title = request.POST['title']
            slogan = request.POST['slogan']
            addHeadline = Home(title=title, paragraph=slogan)
            addHeadline.save()
            return redirect('headline')
        return render(request, 'add-page/add_headline.html')
    
    def add_about_content(request):
        if request.method =='POST':
            body_text = request.POST['body_text']

            about_text = About(About_me = body_text)
            about_text.save()
            return redirect('about_me_sections')
        return render(request, 'add-page/add_about_content.html')
    
class Edits:
    def edit_products(request,id):
        if request.method == "POST":
            ed_show_product = Product.objects.get(id=id)
            ed_show_product.product_name = request.POST['product_name']
            ed_show_product.description = request.POST['description']
            ed_show_product.price = request.POST['price']
            ed_show_product.VAT = request.POST['vat']
            ed_show_product.save()
            messages.info(request, 'Product Update Successfully')
            return redirect('view_products')
            
        ed_show_product = Product.objects.get(id=id)
        context ={
            'ed_show_Product':ed_show_product
        }
        return render(request, 'add-page/edit_product.html',context)
    
    def edit_headline(request, id):
        if request.method=='POST':
            hd = Home.objects.get(id=id)
            hd.title = request.POST['title']
            hd.paragraph = request.POST['slogan']
            hd.save()
            messages.info(request,'Update Headline Successfully')
            return redirect('headline')

        hd = Home.objects.get(id=id)
        context={
            'hd':hd
        }
        return render(request, 'add-page/edit_headline.html',context)
    
    def change_product_image(request,id):
        if request.method =='POST' and request.FILES:
            img_get = Product.objects.get(id=id)
            new_img = request.FILES['images']
            img_get.image_product =new_img
            img_get.save()
            messages.info(request, 'your new image products is updated successfully')
            return redirect('view_products')

        img_get = Product.objects.get(id=id)
        context = {
            'img_id':img_get
        }
        return render(request, 'add-page/change_product_image.html',context)
    
    def update_about(request,id):
        if request.method=="POST":
            ua = About.objects.get(id=id)
            ua.About_me = request.POST['body_text']
            ua.save()
            messages.info(request, 'Successfully Update')
            return redirect('about_me_sections')
        ua = About.objects.get(id=id)
        context ={
            'ua':ua
        }
        return render(request, 'add-page/update_about.html', context)
        
def delete_about(request,id):
    d_about = About.objects.get(id=id)
    d_about.delete()
    messages.info(request, 'Successfully Delete')
    return redirect('about_me_sections')