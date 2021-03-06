from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  generation = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('pokemon_detail', kwargs={'pokemon_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

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
  # change the default sort
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for pokemon_id: {self.pokemon_id} @{self.url}"