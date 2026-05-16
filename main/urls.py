from django.urls import path
from .views import (
    home,
    create_workout,
    workout_list,
    workout_detail
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
]