from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from django.contrib import messages
from .forms import movieEditForm


# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)
    # or return.render(request,'index.html',{'movie_list':movie})
    #  return HttpResponse('Movie site')


def details(request, movie_id):
    return HttpResponse("This is movie number %s" % movie_id)


def showdetails(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def addMovie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['image']

        movie = Movie(name=name, desc=desc, year=year, image=image)
        movie.save()
        messages.info(request, 'Movie saved Successfully!')
    return render(request, 'addMovie.html')


def editMovie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = movieEditForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'editMovie.html', {'form': form, 'movie': movie})


def deleteMovie(request, movie_id):
    name = (Movie.objects.get(id=movie_id)).name
    print(name)
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, 'deleteMovie.html', {'name': name})
