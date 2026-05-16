from django.contrib import admin
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'muscle_group', 'created_at')
    search_fields = ('name', 'muscle_group')