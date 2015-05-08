from django.db import models

# Create your models here.

class Examinee(models.Model):
    examinee_first_name = models.CharField(max_length=200)
    examinee_last_name = models.CharField(max_length=200)
    examinee_birthdate = models.DateField()

class Exam(models.Model):
    examinee = models.ForeignKey(Examinee)
    exam_date = models.DateField('date of exam')
    exam_time_started = models.TimeField('start time')
    exam_time_ended = models.TimeField()
    
class OnlineTest(models.Model):
    exams = models.ManyToManyField(Exam)
    online_test_name = models.CharField(max_length=50)
    online_test_description = models.CharField(max_length=200)
    
class Question(models.Model):
    EASY = 'E'
    MODERATE = 'M'
    HARD = 'H'
    QUESTION_DIFFICULTY_LEVELS = (
        (EASY, 'Easy'),
        (MODERATE, 'Moderate'),
        (HARD, 'Hard'),
    )
    online_test = models.ForeignKey(OnlineTest)
    question_type = models.CharField(max_length=20)
    question_text = models.CharField(max_length=500)
    question_diffficulty = models.CharField(max_length=15, choices=QUESTION_DIFFICULTY_LEVELS, default=EASY)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_is_correct = models.BooleanField(default=False)
    choice_text = models.CharField(max_length=200)

