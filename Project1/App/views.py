from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserAccount
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from Admin.models import *
from django.core.paginator import Paginator



# Create your views here.
try:
    class Index:
        def index(request):
            headline =  Home.objects.all()
            about = About.objects.all()
            pd = Product.objects.all()
            feedbacks = Feedbacks.objects.all()

            c_p = Paginator(pd, 15)
            page_no = request.GET.get('page')
            products = c_p.get_page(page_no)

            context = {
                'headline':headline,
                'about':about,
                'products':products,
                'feedbacks':feedbacks
            }

            return render(request, 'index.html',context)

    class About1:
        def about(request):
            about = About.objects.all()
            context={
                'about':about
            }
            return render(request, 'about.html',context)

    class Contact:
        def contact(request):
            return render(request, 'contact.html')
        
    class main_Product:
        def product(request):
            product= Product.objects.all()
            context = {
                'products':product
            }
            return render(request, 'product.html',context)

    class Testimonial:
        def testimonial(request):
            
            return render(request, 'testimonial.html')
        
    class ClientSignUP:
        def client_signup(request):
            if request.method == "POST":
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                confirm_password = request.POST['confirm-password']

                if password ==  confirm_password:
                    save_user = UserAccount(User_Name = username, User_Email= email, User_Password = password)
                    save_user.save()
                    return redirect('client_signin')
                
                else:
                    messages.info(request, 'Password did not match.')
                    return redirect('client_signup')

            return render (request, 'account/signup.html')
    class ClientSignIn:
        def client_signin(request):
            if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']

                if not UserAccount.objects.filter(User_Name = username).exists():
                    messages.info(request, 'User Name Does Not exit!!')
                    return redirect('client_signin')
                
                access_account = UserAccount(User_Name=username, User_Password=password)
                if authenticate(access_account) and access_account is not None:
                    login(request, access_account)
                    return redirect('index')
                
                else:
                    messages.info(request, 'Invalid Password**')
                    return redirect('client_signin')
                
            return render (request, 'account/login.html')
    class Customer_Feedbacks:
        def feedback(request):
            if request.method == "POST":
                Username = request.POST['your_name']
                phone = request.POST['phone']
                email = request.POST['email']
                feedback = request.POST['feedback']

                reg_feed = Feedbacks(userName = Username, phoneNo=phone,email=email,messages=feedback)
                reg_feed.save()
                
            return redirect('index')
        
except:
    def internet(request):
        return HttpResponse('Please Check Your Internet')
    

