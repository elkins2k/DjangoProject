from django.urls import path
from . import views

urlpatterns = [
    path('', views.chapter_list, name='chapter_list'),
    path('chapters', views.chapter_list, name='chapter_list'),
    path('chapters/new', views.chapter_create, name='chapter_create'),
    path('chapters/<int:pk>', views.chapter_detail, name='chapter_detail'),
    path('chapters/<int:pk>/edit', views.chapter_edit, name='chapter_edit'),
    path('chapters/<int:pk>/delete', views.chapter_delete, name='chapter_delete'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/new', views.recipe_create, name='recipe_create'),
    path('recipes/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:pk>/delete', views.recipe_delete, name='recipe_delete'),
]