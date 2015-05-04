from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=50)
    topic_description = models.CharField(max_length=200)

class Question(models.Model):
    QUESTION_DIFFICULTY_LEVELS = (
        (EASY, 'Easy'),
        (MODERATE, 'Moderate'),
        (HARD, 'Hard'),
    )
    question_type = models.CharField(max_length=20)
    question_text = models.CharField(max_length=500)
    question_diffficulty = models.CharField(max_length=15, choices=QUESTION_DIFFUCULTY_LEVELS, default=EASY)

class Choice(models.Model):
    choice_is_correct = models.BooleanField(default=False)
    choice_text = models.CharField(max_length=200)
    
