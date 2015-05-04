from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=50)
    topic_description = models.CharField(max_length=200)

class Question(models.Model):
    question_type = models.CharField(max_length=20)
    question_text = models.CharField(max__length=500)
