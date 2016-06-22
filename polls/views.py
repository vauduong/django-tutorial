from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Question
#A view will return a HttpResponse object or raise an exception
#this is the simplest view possible in Django. To call the view, we map it to a URL. We make a URLconf in urls.py
#index takes in a request and outputs the five most recently published questions
def index(request):
    #Creates list of 5 most recent questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    all_questions = Question.objects.all()
    context = {'latest_question_list': latest_question_list, 'all_questions' : all_questions}

    #alternatively, render() returns a HttpResponse
    return render(request, 'polls/index.html', context)


#detail takes in request and question_id, tells you which question you're looking at
def detail(request, question_id):
    #alternatively, get_object_or_404() takes in a Django model, any number of keyword arguments.
    #It passes keyword arguments to get(), if there is no object, it raises Http404
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question':question})

#results takes in request and question_id, tells you that you're look at results of that id
def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)

#vote takes in request and question_id, tells you that you're voting on that question
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

