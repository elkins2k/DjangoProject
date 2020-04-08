from django.shortcuts import render, redirect
from .models import Chapter, Recipe
from .forms import ChapterForm, RecipeForm
from django.contrib.auth.decorators import login_required

def chapter_list(request):
    chapters = Chapter.objects.all().extra(order_by=['heading'])
    return render(request, 'chapter_list.html', {'chapters': chapters})

@login_required
def chapter_create(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST,request.FILES)
        if form.is_valid():
            chapter = form.save()
            return redirect('chapter_detail', pk=chapter.pk)
    else:
        form = ChapterForm()
    return render(request, 'chapter_form.html', {'form': form})

def chapter_detail(request, pk):
    chapter = Chapter.objects.get(id=pk)
    return render(request, 'chapter_detail.html', {'chapter': chapter})

@login_required
def chapter_edit(request, pk):
    chapter = Chapter.objects.get(pk=pk)
    if request.method == "POST":
        form = ChapterForm(request.POST, request.FILES, instance=chapter)
        if form.is_valid():
            chapter = form.save()
            return redirect('chapter_detail', pk=chapter.pk)
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'chapter_form.html', {'form': form})

@login_required
def chapter_delete(request, pk):
    Chapter.objects.get(id=pk).delete()
    return redirect('chapter_list')

def recipe_list(request):
    recipes = Recipe.objects.all().extra(order_by=['name'])

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES,instance=recipe)
        if form.is_valid():
            chapter = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    Recipe.objects.get(id=pk).delete()
    return redirect('chapter_list')