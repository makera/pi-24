from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse

from polls.models import Question, Choice


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
