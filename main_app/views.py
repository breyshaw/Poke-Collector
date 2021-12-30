from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Pokemon

# Defining the home view
def home(request):
  return render(request, 'home.html')

# index view, sending dictonary pokemon
def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemon/detail.html', {'pokemon': pokemon})

# inheriting the imported CreateView CBV to create our own class based view to create pokemon
class PokemonCreate(CreateView):
  model = Pokemon
  # the fields attribute is required and can be used to limit or change the ordering of attributes
  fields = '__all__'
  success_url = '/pokemon/'

def about(request):
  return render(request, 'about.html')



