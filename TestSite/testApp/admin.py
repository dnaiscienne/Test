from django.contrib import admin
from testApp.models import Choice, Question, OnlineTest

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
        (None,      {'fields': ['question_text', 'question_difficulty']}),
    ]
    inlines = [ChoiceInline]

class OnlineTestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['online_test_name', 'online_test_description']}),
    ]
    inlines = [QuestionInline]

admin.site.register(OnlineTest, OnlineTestAdmin)
admin.site.register(Question, QuestionAdmin)
