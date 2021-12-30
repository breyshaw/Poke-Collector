from django.shortcuts import render
from .models import Pokemon

# Defining the home view
def home(request):
  return render(request, 'home.html')

# index view, sending dictonary pokemon
def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def about(request):
  return render(request, 'about.html')

