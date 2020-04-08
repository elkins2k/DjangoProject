from django.contrib import admin
from .models import Chapter, Recipe

admin.site.register([Chapter, Recipe])
