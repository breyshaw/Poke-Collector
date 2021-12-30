from django.shortcuts import render
#For testing purposes
from django.http import HttpResponse

# Defining the home view
def home(request):
  return HttpResponse('<h1>Gotta Catch Em All!</h1>')

def pokemon_index(request):
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def about(request):
  return render(request, 'about.html')

class Pokemon:
  def __init__(self, name, type, description, generation):
    self.name = name
    self.type = type
    self.description = description
    self.generation = generation

# for testing
pokemon = [
  Pokemon('Bulbasaur','Grass','Cute plant boi', 1),
  Pokemon('Charmander','Fire','Cute fire boi', 1),
  Pokemon('Squirtle','Water','Cute turtle boi', 1),
]

