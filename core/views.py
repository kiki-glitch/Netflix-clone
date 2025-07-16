from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
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
        catch(err):


    else:
        return render(request,'signup.html')