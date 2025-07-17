from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie, MovieList
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import re

# Create your views here.
@login_required(login_url='login')
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }

    return render(request, 'index.html', context)

def movie(request,pk):
    movie_uuid = pk
    movie_details = Movie.objects.get(uuid=movie_uuid)

    context ={
        'movie_details': movie_details
    }
    
    return render(request,'movie.html',context)

def my_list(request):
    
    movie_list = MovieList.objects.filter(owner_user=request.user)
    user_movie_list = []

    for movie in movie_list:
        user_movie_list.append(movie.movie)
        context = {
            'movies': user_movie_list
        }
    
    return render(request, 'my_list.html', context)


def add_to_list(request):
    if request.method == 'POST':
        movie_url_id = request.POST.get('movie_id')

        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

        match = re.search(uuid_pattern, movie_url_id)
        movie_id = match.group() if match else None

        if not movie_id:
            return JsonResponse({'status': 'error', 'message': 'Invalid UUID provided'}, status=400)

        movie = get_object_or_404(Movie, uuid=movie_id)
        movie_list, created = MovieList.objects.get_or_create(
            owner_user=request.user,
            movie=movie
        )

        if created:
            response_data = {'status': 'success', 'message':'Added ✓'}
        else:
            response_data = {'status': 'info', 'message':'Movie already in list'}
        
        return JsonResponse(response_data)
    else:
        response_data = JsonResponse({'status': 'info', 'message':'Invalid request'}, status=405)

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