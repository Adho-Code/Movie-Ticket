from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def index(request):
    return render(request, 'index.html')

def home(request,id):

    mov = Movable.objects.all()

    post = Post.objects.filter(movie_id=id)

    avail = Available.objects.all()

    post = Post.objects.filter(movie_id=id)
    return render(request, 'home.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

def search_movie(request):
    
    if 'movie' in request.GET and request.GET["movie"]:
        search_term = request.GET.get("movie")
        searched_movie = Movie.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',locals())

