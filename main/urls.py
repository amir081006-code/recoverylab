from django.urls import path
from .views import (
    home,
    create_workout,
    workout_list,
    workout_detail,
    body_stats,
    dashboard,
    add_body_measurement,
    add_workout_set,
    add_recovery,
)

urlpatterns = [
    path('', home, name='home'),

    path(
        'add-recovery/',
        add_recovery,
        name='add_recovery'
    ),

    path(
        'add-workout-set/',
        add_workout_set,
        name='add_workout_set'
    ),

    path(
        'add-body-measurement/',
        add_body_measurement,
        name='add_body_measurement'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'create-workout/',
        create_workout,
        name='create_workout'
    ),

    path(
        'workouts/',
        workout_list,
        name='workout_list'
    ),

    path(
        'workout/<int:workout_id>/',
        workout_detail,
        name='workout_detail'
    ),

    path(
        'body-stats/',
        body_stats,
        name='body_stats'
    ),
]