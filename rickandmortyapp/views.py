from django.shortcuts import render
from rickandmortyapp.models import Character

# Create your views here.


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'rickandmortyapp/home.html', {'characters': characters})
