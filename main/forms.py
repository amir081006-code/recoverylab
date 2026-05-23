from django import forms
from .models import Workout
from .models import BodyMeasurement
from .models import WorkoutSet
from .models import RecoveryMetric

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout

        fields = [
            'title',
            'workout_date',
            'duration',
            'fatigue_level',
            'notes',
        ]

        widgets = {
            'workout_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

class BodyMeasurementForm(forms.ModelForm):

    class Meta:

        model = BodyMeasurement

        fields = [
            'weight',
            'body_fat',
            'muscle_mass',
            'measurement_date'
        ]

class WorkoutSetForm(forms.ModelForm):

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

class RecoveryMetricForm(forms.ModelForm):

    class Meta:

        model = RecoveryMetric

        fields = [
            'workout',
            'sleep_hours',
            'stress_level',
            'energy_level',
            'recovery_score'
        ]