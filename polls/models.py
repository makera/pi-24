import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="текст вопроса")
    pub_date = models.DateTimeField(verbose_name="дата публикации")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Опубликован недавно?",
    )
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Выбор ответа"
        verbose_name_plural = "Выборы ответа"