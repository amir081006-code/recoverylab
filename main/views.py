from django.shortcuts import render


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

from .models import Workout, WorkoutSet, RecoveryMetric


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