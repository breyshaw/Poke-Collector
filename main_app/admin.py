from django.contrib import admin
from .models import Pokemon

# Registering models here so that they can be accessed in the admin portal.
admin.site.register(Pokemon)
