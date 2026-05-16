from django.urls import path
from .views import (
    home,
    create_workout,
    workout_list,
    workout_detail,
    body_stats
)

urlpatterns = [
    path('', home, name='home'),
    path('create-workout/', create_workout, name='create_workout'),
    path('workouts/', workout_list, name='workout_list'),

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