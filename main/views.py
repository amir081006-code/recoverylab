from django.shortcuts import render
from django.db.models import Avg
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

from .forms import (
    WorkoutForm,
    BodyMeasurementForm,
    WorkoutSetForm,
    RecoveryMetricForm
)
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

def add_workout_set(request):

    if request.method == 'POST':

        form = WorkoutSetForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = WorkoutSetForm()

    return render(
        request,
        'main/add_workout_set.html',
        {
            'form': form
        }
    )

def add_recovery(request):

    if request.method == 'POST':

        form = RecoveryMetricForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = RecoveryMetricForm()

    return render(
        request,
        'main/add_recovery.html',
        {
            'form': form
        }
    )

def add_body_measurement(request):

    if request.method == 'POST':

        form = BodyMeasurementForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = BodyMeasurementForm()

    return render(
        request,
        'main/add_body_measurement.html',
        {
            'form': form
        }
    )
    
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

def dashboard(request):

    workouts_count = Workout.objects.count()

    latest_weight = BodyMeasurement.objects.last()

    average_fatigue = Workout.objects.aggregate(
        Avg('fatigue_level')
    )

    latest_recovery = RecoveryMetric.objects.last()

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

    workout_sets = WorkoutSet.objects.all()

    total_volume = 0

    for item in workout_sets:

        volume = (
            item.sets *
            item.reps *
            item.weight
        )

        total_volume += volume

    recommendations = []

    if average_fatigue['fatigue_level__avg']:

        if average_fatigue['fatigue_level__avg'] > 8:
            recommendations.append(
                'Высокий уровень усталости. '
                'Рекомендуется снизить нагрузку.'
            )

    if latest_recovery:

        if latest_recovery.sleep_hours < 6:
            recommendations.append(
                'Недостаток сна может ухудшать восстановление.'
            )

        if (
            latest_recovery.sleep_hours < 6
            and
            average_fatigue['fatigue_level__avg']
            and
            average_fatigue['fatigue_level__avg'] > 7
        ):

            recommendations.append(
                'Высокая усталость может быть '
                'связана с недостатком сна.'
            )

        if latest_recovery.recovery_score < 5:
            recommendations.append(
                'Низкий recovery score. '
                'Организм восстанавливается недостаточно эффективно.'
            )

        if latest_recovery.stress_level > 7:
            recommendations.append(
                'Высокий уровень стресса '
                'может негативно влиять на тренировки.'
            )

        if (
            average_fatigue['fatigue_level__avg']
            and
            average_fatigue['fatigue_level__avg'] > 8
            and
            latest_recovery.recovery_score < 5
            and
            latest_recovery.stress_level > 7
        ):

            recommendations.append(
                'Обнаружены признаки накопленной '
                'усталости и возможного переутомления.'
            )

    recent_workouts = WorkoutSet.objects.order_by(
        '-id'
    )[:5]

    recent_volume = 0

    for item in recent_workouts:

        recent_volume += (
            item.sets *
            item.reps *
            item.weight
        )

    if recent_volume > 20000:

        recommendations.append(
            'За последнее время тренировочная '
            'нагрузка значительно увеличилась.'
        )

    if (
        recent_volume > 20000
        and
        latest_recovery
        and
        latest_recovery.recovery_score > 7
    ):

        recommendations.append(
            'Нагрузка увеличивается при хорошем '
            'уровне восстановления. Прогресс выглядит устойчивым.'
        )

    recent_recoveries = RecoveryMetric.objects.order_by(
        '-id'
    )[:3]

    if len(recent_recoveries) == 3:

        recovery_values = [
            item.recovery_score
            for item in recent_recoveries
        ]

        if (
            recovery_values[0] <
            recovery_values[1] <
            recovery_values[2]
        ):

            recommendations.append(
                'Recovery score снижается '
                'несколько тренировок подряд.'
            )

    if not recommendations:
        recommendations.append(
            'Показатели восстановления находятся '
            'в нормальном диапазоне.'
        )

    context = {
        'workouts_count': workouts_count,
        'latest_weight': latest_weight,
        'average_fatigue': average_fatigue,
        'latest_recovery': latest_recovery,
        'chart': chart,
        'total_volume': total_volume,
        'recommendations': recommendations,
    }

    return render(
        request,
        'main/dashboard.html',
        context
    )