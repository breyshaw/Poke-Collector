from django.urls import path
from . import views

urlpatterns = [
  # This defines a root path using an emtpy string and maps it to the view.home function
  # The name='home' kwarg is optional but will come in handly referencing the URL from other parts of the app.
  path('', views.home, name='home'),
  # Trailing slashes are convention for Django
  path('about/', views.about, name='about'),
  path('pokemon/', views.pokemon_index, name='pokemon_index'),
  path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name="pokemon_detail"),
  # CBV examples
  path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
  path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
  path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
]