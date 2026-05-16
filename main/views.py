from django.shortcuts import render
import pandas as pd
import plotly.express as px
from .models import (
    Workout,
    WorkoutSet,
    RecoveryMetric,
    BodyMeasurement
)

def home(request):
    return render(request, 'main/home.html') 

from .forms import WorkoutForm
from django.shortcuts import redirect


def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = WorkoutForm()

    return render(request, 'main/create_workout.html', {
        'form': form
    })


def workout_list(request):
    workouts = Workout.objects.all()

    return render(request, 'main/workout_list.html', {
        'workouts': workouts
    })

def workout_detail(request, workout_id):

    workout = Workout.objects.get(id=workout_id)

    workout_sets = WorkoutSet.objects.filter(
        workout=workout
    )

    recovery = RecoveryMetric.objects.filter(
        workout=workout
    ).first()

    return render(request, 'main/workout_detail.html', {
        'workout': workout,
        'workout_sets': workout_sets,
        'recovery': recovery,
    })

def body_stats(request):

    measurements = BodyMeasurement.objects.all().order_by(
        'measurement_date'
    )

    dates = []
    weights = []

    for item in measurements:
        dates.append(item.measurement_date)
        weights.append(item.weight)

    df = pd.DataFrame({
        'Дата': dates,
        'Вес': weights
    })

    fig = px.line(
        df,
        x='Дата',
        y='Вес',
        title='Динамика веса'
    )

    chart = fig.to_html()

    return render(request, 'main/body_stats.html', {
        'chart': chart
    })