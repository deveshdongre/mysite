from django.shortcuts import render
from django.http import HttpResponse  # if we use render we no longer need this
from django.template import loader  # if we use render we no longer need this
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # the below after content is shortcut | template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # this is combine shortcut step which import
    return render(request, 'polls/index.html', context)
    # the above method is short cut | return HttpResponse(template.render(context, request))
    #   return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
