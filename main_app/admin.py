from django.contrib import admin
from .models import Pokemon, Feeding, Toy

# Registering models here so that they can be accessed in the admin portal.
admin.site.register(Pokemon)
admin.site.register(Feeding)
admin.site.register(Toy)
