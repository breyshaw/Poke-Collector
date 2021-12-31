from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Toy
from .forms import FeedingForm

# Defining the home view
def home(request):
  return render(request, 'home.html')

# index view, sending dictonary pokemon
def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  # Get the toys the mon doesn't have
  toys_pokemon_doesnt_have = Toy.objects.exclude(id__in = pokemon.toys.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'pokemon/detail.html', {
    # include the cat and feeding_form in the context
    'pokemon': pokemon, 'feeding_form': feeding_form, 'toys': toys_pokemon_doesnt_have
  })

def add_feeding(request, pokemon_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.pokemon_id = pokemon_id
    new_feeding.save()
    # Always be sure to redirect instead of render if data has been changed in the database.
  return redirect('pokemon_detail', pokemon_id=pokemon_id)

# inheriting the imported CreateView CBV to create our own class based view to create pokemon
class PokemonCreate(CreateView):
  model = Pokemon
  # the fields attribute is required and can be used to limit or change the ordering of attributes
  fields = ['name', 'type', 'description', 'generation']
  success_url = '/pokemon/'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['name', 'type', 'description', 'generation']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, pokemon_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Pokemon.objects.get(id=pokemon_id).toys.add(toy_id)
  return redirect('pokemon_detail', pokemon_id=pokemon_id)

def about(request):
  return render(request, 'about.html')