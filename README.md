# RecoveryLab

RecoveryLab — intelligent sports recovery assistant, разработанный на Django.

Проект помогает спортсмену:

* отслеживать тренировочную нагрузку,
* анализировать восстановление,
* контролировать fatigue,
* следить за body metrics,
* получать рекомендации по восстановлению.

---

# Возможности

## Training Management

* создание тренировок
* добавление упражнений
* tracking sets/reps/weight
* расчет training volume

## Recovery Analytics

* анализ сна
* анализ уровня стресса
* recovery score monitoring
* fatigue tracking

## Intelligent Recommendations

RecoveryLab анализирует:

* fatigue
* sleep quality
* stress level
* training volume
* recovery trends

и выдает рекомендации пользователю.

Примеры:

* предупреждение о переутомлении
* рекомендации снизить нагрузку
* анализ недостатка сна
* detection of accumulated fatigue

## Body Metrics

* tracking веса
* body fat percentage
* muscle mass tracking
* график изменения веса

## Analytics Dashboard

* interactive Plotly graphs
* dashboard cards
* recovery analytics
* volume statistics
* trend analysis

---

# Technologies

* Python
* Django
* Bootstrap 5
* Plotly
* Pandas
* SQLite

---

# Database Structure

Основные модели проекта:

* Workout
* Exercise
* WorkoutSet
* RecoveryMetric
* BodyMeasurement

Проект использует relational database architecture и связи между тренировками, упражнениями и recovery metrics.

---

# How To Run

## 1. Clone repository

```bash
git clone <your-repository-url>
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run server

```bash
python manage.py runserver
```

---

# Screenshots

## Dashboard

* analytics cards
* recovery recommendations
* weight analytics
* training statistics

## ER Diagram

![ER Diagram](screenshots/er_diagram.png)

---

# Project Goal

Цель проекта — создание системы анализа тренировочной нагрузки и восстановления спортсмена с элементами intelligent recommendation system.

RecoveryLab не является просто дневником тренировок. Система анализирует состояние спортсмена и помогает отслеживать признаки переутомления и восстановления.

---

# Future Improvements

* user authentication
* multi-user support
* advanced analytics
* nutrition tracking
* AI-based recommendations
* export analytics reports
