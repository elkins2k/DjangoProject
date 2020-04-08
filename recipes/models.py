from django.db import models

class Chapter(models.Model):
  heading = models.CharField(max_length=10)
  thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
  description = models.TextField()

  def __str__(self):
      return self.heading

class Recipe(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/', blank=True, null=True)
  chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, related_name='recipes')
  ingredients = models.TextField()
  directions = models.TextField()

  def __str__(self):
      return self.name

# class Component(models.Model):
#   amount = models.CharField(max_length=5)
#   ingredient = models.CharField(max_length=20)
#   recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name='recipe')

#   def __str__(self):
#       return self.ingredient
  