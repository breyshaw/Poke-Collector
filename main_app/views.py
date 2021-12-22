from django.shortcuts import render
#For testing purposes
from django.http import HttpResponse

# Defining the home view
def home(request):
  return HttpResponse('<h1>Gotta Catch Em All!</h1>')

def about(request):
  return render(request, 'about.html')

