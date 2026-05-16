from django.db import models


class Exercise(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название упражнения'
    )

    muscle_group = models.CharField(
        max_length=100,
        verbose_name='Группа мышц'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class Workout(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название тренировки'
    )

    workout_date = models.DateField(
        verbose_name='Дата тренировки'
    )

    duration = models.PositiveIntegerField(
        verbose_name='Длительность (мин)'
    )

    fatigue_level = models.IntegerField(
        verbose_name='Уровень усталости'
    )

    notes = models.TextField(
        blank=True,
        verbose_name='Заметки'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

class WorkoutSet(models.Model):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        verbose_name='Тренировка'
    )

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        verbose_name='Упражнение'
    )

    sets = models.PositiveIntegerField(
        verbose_name='Количество подходов'
    )

    reps = models.PositiveIntegerField(
        verbose_name='Повторения'
    )

    weight = models.FloatField(
        verbose_name='Вес (кг)'
    )

    rpe = models.IntegerField(
        verbose_name='RPE'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.exercise} - {self.weight} кг'

    class Meta:
        verbose_name = 'Подход упражнения'
        verbose_name_plural = 'Подходы упражнений'