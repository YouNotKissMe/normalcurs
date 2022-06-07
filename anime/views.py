from .models import Anime, Genre, Type, Anonce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def main_animes(request):
    if 'search' in request.GET and request.GET['search']:
        if Anime.objects.filter(name__icontains=request.GET['search']):
            anime = Anime.objects.filter(name__icontains=request.GET['search'])
        else:
            anime = Anime.objects.all()
    else:
        anime = Anime.objects.all()
    genre = Genre.objects.all()
    type = Type.objects.all()
    an = Anonce.objects.all()
    return render(request, 'all_anime.html', {'anime': anime, 'an': an, 'type': type, 'genre': genre})


def genre(request, pk):
    anime = Anime.objects.filter(genre__pk=pk)
    user = request.user
    return render(request, 'genre.html', {'anime': anime, 'user': user})


def type(request, pk):
    anime = Anime.objects.filter(typeAnime__pk=pk)
    user = request.user
    return render(request, 'genre.html', {'anime': anime, 'user': user})


def anonce(request, pk):
    anime = Anime.objects.filter(status__pk=pk)
    user = request.user
    return render(request, 'genre.html', {'anime': anime, 'user': user})


def anime_page(request, pk):
    anime = Anime.objects.get(pk=pk)

    return render(request, 'anime_page.html', {'anime': anime})


def anime_add(request, pk):
    an = User.objects.get(pk=request.user.pk)
    an.anime_set.add(Anime.objects.get(pk=pk))
    return redirect('profile')


