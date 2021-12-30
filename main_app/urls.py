from django.urls import path
from . import views

urlpatterns = [
  # This defines a root path using an emtpy string and maps it to the view.home function
  # The name='home' kwarg is optional but will come in handly referencing the URL from other parts of the app.
  path('', views.home, name='home'),
  # Trailing slashes are convention for Django
  path('about/', views.about, name='about'),
  path('pokemon/', views.pokemon_index, name='pokemon_index')
]