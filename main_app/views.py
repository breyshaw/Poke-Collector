from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from .models import Pokemon, Toy, Photo
import uuid
import boto3
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'poke-collector-app'

# Defining the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

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
    # include the pokemon and feeding_form in the context
    'pokemon': pokemon, 'feeding_form': feeding_form, 'toys': toys_pokemon_doesnt_have
  })

def add_feeding(request, pokemon_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the pokemon_id assigned
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

def add_photo(request, pokemon_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to pokemon_id or pokemon (if you have a pokemon object)
      photo = Photo(url=url, pokemon_id=pokemon_id)
      # Remove old photo if it exists
      pokemon_photo = Photo.objects.filter(pokemon_id=pokemon_id)
      if pokemon_photo.first():
        pokemon_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('pokemon_detail', pokemon_id=pokemon_id)

