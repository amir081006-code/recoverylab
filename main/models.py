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