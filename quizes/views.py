from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import *
from django.contrib.auth.models import User
from results.models import *


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


def save_quiz_view(request, pk):
    print(request.POST)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = request.POST
        # print('Ajax request detected')
        # transfer query  dict to ordinary dict
        data_ = dict(data.lists())
        # print((type(data_)))
        #
        # print(type(data))
        # print('Print statement executed')

        # return ques and ans
        data_.pop('csrfmiddlewaretoken')
        print(data_)
        questionss = []
        for d in data_.keys():
            print('keys', d)
            question = Question.objects.get(text=d)
            questionss.append(question)

        # list of question obj
        print(questionss)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multipler = 100 / quiz.number_of_qus
        results = []
        correct_answer = None

        # basicaly it itreate the question dictonary and get key  wise ans means que wise ans
        for q in questionss:
            a_selected = request.POST.get(q.text)
            # print("ans", a_selected)
            if (a_selected != ""):
                # it  get all answer for patricullar que
                question_ans = Answer.objects.filter(question=q)
                # loop all answer
                for a in question_ans:
                    # compare answer
                    if a_selected == a.text:
                        # value of ans in db is true than +1
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                        else:
                            if a.correct:
                                correct_answer = a.text
                # question : ans : selected ans and this the case when user selected the answer
                results.append({str(q): {'correcct_ans': correct_answer, 'answerd': a_selected}})
            else:
                results.append({str(q): 'Not Answerd'})

        score_ = score * multipler
        Result.objects.create(quiz=quiz, user=user, score=score_)
        if score_ >= quiz.requierd_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'result': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'result': results})
