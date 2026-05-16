from django import forms
from .models import Workout


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