from django.contrib import admin
from testApp.models import *

from django.core.urlresolvers import reverse

# Register your models here.
    
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    max_num = 5

class QuestionInline(admin.TabularInline):
    show_change_link = True
    model = Question
    exclude = ('question_type',)
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['online_test', 'question_text', 'question_difficulty']}),
    ]
    inlines = [ChoiceInline]
##    list_filter = ['online_test']
    def get_model_perms(self, request):
        return{}

class OnlineTestAdmin(admin.ModelAdmin):
    
    def question_link(self, obj):
        url = reverse('admin:testApp_question_changelist')
        return '<a href="%s?online_test_id=%s">See Questions</a>' % (url, obj.pk)
    question_link.allow_tags = True
    list_display = ('online_test_name', 'question_link',)
    
    fieldsets = [
        (None,      {'fields': ['online_test_name', 'online_test_description', 'exam_type']}),
    ]
    inlines = [QuestionInline]
	
admin.site.register(Examinee)
admin.site.register(ExamType)
admin.site.register(Exam)
admin.site.register(OnlineTest, OnlineTestAdmin)
admin.site.register(Question, QuestionAdmin)
