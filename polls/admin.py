from django.contrib import admin
from .models import Question, Choice

# Django offers a tabular way of displaying inline related objects. To use it, change the ChoiceInline declaration to read:
# class ChoiceInline(admin.TabularInline):


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('date informed', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
# this list_dispaly menthod will dispaly the values Question admin page with the above tabular format
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
