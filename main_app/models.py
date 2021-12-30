from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  generation = models.IntegerField()
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('pokemon_detail', kwargs={'pokemon_id': self.id})

class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  def __str__(self):
  # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
