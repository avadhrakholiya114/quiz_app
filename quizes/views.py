from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse


# Create your views here.

class Quiz_list(ListView):
    model = Quiz
    template_name = 'quizes/main.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    # what question are related to quiz
    questions = []
    for q in quiz.get_question():
        # what answers related to quiz.
        answers = []
        for a in q.get_ans():
            answers.append(a.text)
        # str(q): answers for key value
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time
    })
