from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_ac(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg='username and password didnot mathch!'
        else:
            msg = 'Error Validating of Form'
    return render(request, 'login.html',{'form':form, 'msg':msg})

def register(request):
    msg=None
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form= SignUpForm()

    return render(request, 'register.html',{'form':form,'msg':msg})

def home(request):
    return redirect(request, 'home.html')