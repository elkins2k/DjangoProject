import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Chapter(models.Model):
  heading = models.CharField(max_length=10)
  thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
  description = models.TextField()

  def save(self, *args, **kwargs):
    if not self.id:
      self.thumbnail = self.compressImage(self.thumbnail)
    super(Chapter, self).save(*args, **kwargs)
  
  def compressImage(self, thumbnail):
    imageTemporary = Image.open(thumbnail)
    outputIoStream = BytesIO()
    imageTemporaryResized = imageTemporary.resize( (300,300) ) 
    imageTemporary.save(outputIoStream , format='JPEG', quality=75)
    outputIoStream.seek(0)
    thumbnail = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % thumbnail.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    return thumbnail
  
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
  