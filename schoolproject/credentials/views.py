
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'home.html')
def confirm(request):
    return render(request,'confirm.html')
def store(request):
    return render(request,'store.html')

def order(request):
    return render(request,'order.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect('register')

            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            user.save()
            return redirect('login')


        else:
            messages.info(request, "password missmatch")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('store')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')