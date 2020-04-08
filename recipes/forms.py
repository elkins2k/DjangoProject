from django import forms
from .models import Chapter, Recipe

class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ('heading','thumbnail','description',)

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name','image','chapter','ingredients','directions',)