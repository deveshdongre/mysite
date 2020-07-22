from django.shortcuts import render, get_object_or_404
# if we use render we no longer need this
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader  # if we use render we no longer need this
from .models import Question
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# commented views are not generic, they are the traditional one(hard way)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # the below after content is shortcut | template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # this is combine shortcut step which import
#     return render(request, 'polls/index.html', context)
#     # the above method is short cut | return HttpResponse(template.render(context, request))
#     #   return HttpResponse("Hello, world. You're at the polls index.")


# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        ###+++IMPORTANT+++###
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'