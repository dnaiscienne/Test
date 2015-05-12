from django.test import TestCase

# Create your tests here.

from testApp.models import Question

class QuestionTests(TestCase):

    def question_str(self):
        question = Question(question_text='Is this a question?')
        self.assertEquals(
            str(question), 'Is this a question?',
        )
            
