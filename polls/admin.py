from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', "was_published_recently"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ['question_text']

admin.site.register(Choice)
