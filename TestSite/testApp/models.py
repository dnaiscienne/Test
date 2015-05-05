from django.db import models

# Create your models here.

class OnlineTest(models.Model):
    online_test_name = models.CharField(max_length=50)
    online_test_description = models.CharField(max_length=200)
    
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
    
class Exam(models.Model):
    exam_date= models.DateField('date of exam')
    exam_time_started = models.TimeField('start time')
    exam_time_ended = models.TimeField()

class Examinee(models.Model):
    examinee_first_name = models.CharField()
    examinee_last_name = models.CharField()
    examinee_birthdate = models.DateField()
