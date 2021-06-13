from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from .models import Question
# Create your views here.
def homepage(request):
    questions=Question.objects.all().order_by('-created_at')
    context={
        'questions':questions
    }
    return render(request, 'homepage.html',context)

def question(request, question_id):
    q1=Question.objects.get(pk=question_id)
    context={
        'q1':q1
    }
    return render(request,'quest.html',context)

def student(request):
    return render(request, 'student.html')

def tutor(request):
    return render(request, 'tutor.html')

def result(request):
    context={}
    context['form']=InputForm()
    return render(request, 'result.html' ,context)