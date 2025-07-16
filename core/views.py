from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_to_list(request):
    pass

def login(request):
    if request.user.is_authenticated:
        return redirect('/') 
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not username or not password:
            error_message = 'All fields are required.'
            messages.info(request, error_message)
            return redirect(login)
        
        user = auth.authenticate(request,username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            messages.info(request, error_message)
            return redirect(login)
    else: 
        return render(request, 'login.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/') 
    
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not username or not email or not password or not password2:
            error_message = 'All fields are required.'
            messages.info(request, error_message)
            return redirect(signup)
      
        # Check if passwords match
        if password != password2:
            error_message = 'Passwords do not match.'
            messages.info(request, error_message)
            return redirect(signup)

        try:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')

        except Exception as e:
            error_message = f'Unexpected error: {str(e)}'
            messages.info(request, error_message)
            return redirect('signup')

    else:
        return render(request,'signup.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')