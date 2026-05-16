from django.contrib import admin
from .models import Exercise, Workout, WorkoutSet


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'muscle_group', 'created_at')
    search_fields = ('name', 'muscle_group')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'workout_date', 'duration', 'fatigue_level')
    search_fields = ('title',)

@admin.register(WorkoutSet)
class WorkoutSetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'workout',
        'exercise',
        'sets',
        'reps',
        'weight',
        'rpe'
    )

    search_fields = (
        'exercise__name',
        'workout__title',
    )