from django import forms

from .models import BodyMeasurement
from .models import RecoveryMetric
from .models import Workout
from .models import WorkoutSet


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            widget = field.widget

            if isinstance(widget, forms.Select):
                control_class = 'form-select'
            elif isinstance(widget, forms.CheckboxInput):
                control_class = 'form-check-input'
            else:
                control_class = 'form-control'

            current_class = widget.attrs.get('class', '')
            widget.attrs['class'] = f'{current_class} {control_class}'.strip()
            widget.attrs.setdefault('aria-label', field.label)

            if not isinstance(widget, forms.Select):
                widget.attrs.setdefault('placeholder', field.label)

            if isinstance(widget, forms.Textarea):
                widget.attrs.setdefault('rows', 4)


class WorkoutForm(StyledModelForm):

    class Meta:
        model = Workout

        fields = [
            'title',
            'workout_date',
            'duration',
            'fatigue_level',
            'notes',
        ]

        labels = {
            'title': 'Название тренировки',
            'workout_date': 'Дата тренировки',
            'duration': 'Длительность, мин',
            'fatigue_level': 'Усталость, 1-10',
            'notes': 'Заметки',
        }

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Например: Силовая тренировка'}
            ),
            'workout_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'duration': forms.NumberInput(
                attrs={'min': 1, 'placeholder': '60'}
            ),
            'fatigue_level': forms.NumberInput(
                attrs={'min': 1, 'max': 10, 'placeholder': '7'}
            ),
            'notes': forms.Textarea(
                attrs={'placeholder': 'Коротко о нагрузке, самочувствии и ощущениях'}
            ),
        }


class BodyMeasurementForm(StyledModelForm):

    class Meta:

        model = BodyMeasurement

        fields = [
            'weight',
            'body_fat',
            'muscle_mass',
            'measurement_date'
        ]

        labels = {
            'weight': 'Вес, кг',
            'body_fat': 'Процент жира',
            'muscle_mass': 'Мышечная масса, кг',
            'measurement_date': 'Дата измерения',
        }

        widgets = {
            'weight': forms.NumberInput(
                attrs={'step': '0.1', 'min': 0, 'placeholder': '82.4'}
            ),
            'body_fat': forms.NumberInput(
                attrs={'step': '0.1', 'min': 0, 'max': 100, 'placeholder': '14.5'}
            ),
            'muscle_mass': forms.NumberInput(
                attrs={'step': '0.1', 'min': 0, 'placeholder': '39.0'}
            ),
            'measurement_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class WorkoutSetForm(StyledModelForm):

    class Meta:

        model = WorkoutSet

        fields = [
            'workout',
            'exercise',
            'sets',
            'reps',
            'weight',
            'rpe'
        ]

        labels = {
            'workout': 'Тренировка',
            'exercise': 'Упражнение',
            'sets': 'Подходы',
            'reps': 'Повторы',
            'weight': 'Вес, кг',
            'rpe': 'RPE, 1-10',
        }

        widgets = {
            'sets': forms.NumberInput(
                attrs={'min': 1, 'placeholder': '4'}
            ),
            'reps': forms.NumberInput(
                attrs={'min': 1, 'placeholder': '8'}
            ),
            'weight': forms.NumberInput(
                attrs={'step': '0.5', 'min': 0, 'placeholder': '80'}
            ),
            'rpe': forms.NumberInput(
                attrs={'min': 1, 'max': 10, 'placeholder': '8'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['workout'].empty_label = 'Выберите тренировку'
        self.fields['exercise'].empty_label = 'Выберите упражнение'


class RecoveryMetricForm(StyledModelForm):

    class Meta:

        model = RecoveryMetric

        fields = [
            'workout',
            'sleep_hours',
            'stress_level',
            'energy_level',
            'mood',
            'recovery_score'
        ]

        labels = {
            'workout': 'Тренировка',
            'sleep_hours': 'Сон, часов',
            'stress_level': 'Стресс, 1-10',
            'energy_level': 'Энергия, 1-10',
            'mood': 'Самочувствие',
            'recovery_score': 'Recovery Score, 1-10',
        }

        widgets = {
            'sleep_hours': forms.NumberInput(
                attrs={'step': '0.5', 'min': 0, 'max': 24, 'placeholder': '7.5'}
            ),
            'stress_level': forms.NumberInput(
                attrs={'min': 1, 'max': 10, 'placeholder': '4'}
            ),
            'energy_level': forms.NumberInput(
                attrs={'min': 1, 'max': 10, 'placeholder': '7'}
            ),
            'mood': forms.TextInput(
                attrs={'placeholder': 'Например: бодро, напряженно, спокойно'}
            ),
            'recovery_score': forms.NumberInput(
                attrs={'step': '0.1', 'min': 1, 'max': 10, 'placeholder': '8.2'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['workout'].empty_label = 'Выберите тренировку'
