# Техническое задание — RecoveryLab

## Название проекта

RecoveryLab — intelligent sports recovery assistant.

---

# Описание проекта

RecoveryLab — веб-приложение для анализа тренировочной нагрузки и восстановления спортсмена.

Система позволяет:
- отслеживать тренировки,
- анализировать fatigue,
- контролировать recovery metrics,
- вести body metrics,
- получать рекомендации по восстановлению.

Проект разработан на Django с использованием relational database architecture.

---

# Цель проекта

Создание системы мониторинга тренировок и восстановления спортсмена с элементами аналитики и recommendation system.

---

# Основной функционал

## 1. Управление тренировками

Пользователь может:
- создавать тренировки,
- добавлять упражнения,
- указывать:
  - подходы,
  - повторения,
  - рабочий вес,
  - RPE.

---

## 2. Recovery Analytics

Система анализирует:
- сон,
- уровень стресса,
- fatigue,
- recovery score,
- тренировочную нагрузку.

---

## 3. Body Metrics Tracking

Пользователь может:
- добавлять вес,
- процент жира,
- мышечную массу.

Система строит графики изменения веса.

---

## 4. Recommendation System

RecoveryLab анализирует показатели пользователя и выдает рекомендации.

Примеры:
- предупреждение о переутомлении,
- рекомендации снизить нагрузку,
- анализ недостатка сна,
- detection of accumulated fatigue.

---

## 5. Dashboard Analytics

Dashboard отображает:
- training volume,
- recovery score,
- average fatigue,
- body metrics,
- графики Plotly,
- рекомендации системы.

---

# Используемые технологии

- Python
- Django
- Bootstrap 5
- Plotly
- Pandas
- SQLite

---

# Архитектура базы данных

Проект использует relational database architecture.

Основные модели:
- Workout
- Exercise
- WorkoutSet
- RecoveryMetric
- BodyMeasurement

Связи между моделями реализованы через ForeignKey.

---

# Интерфейс системы

Система включает:
- dashboard,
- формы ввода данных,
- аналитику,
- responsive navigation,
- modern dark UI.

---

# Нефункциональные требования

## Производительность
- корректная работа с SQLite database
- обработка аналитики и графиков

## Интерфейс
- responsive design
- поддержка мобильных экранов
- современный UI/UX

## Надежность
- использование Django ORM
- валидация форм
- защита CSRF

---

# Планируемые улучшения

- авторизация пользователей
- multi-user system
- advanced analytics
- nutrition tracking
- AI-based recommendations
- export reports

---

# Результат проекта

В результате разработки создано веб-приложение для анализа тренировочной нагрузки и восстановления спортсмена с системой рекомендаций и аналитическим dashboard.