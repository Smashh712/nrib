from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    page = request.GET.get('page', '1') # pybo/?page=1 : default=1
    
    question_list = Question.objects.order_by('-create_date')
    
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        #question = get_object_or_404(Question, pk=question_id)
        context = {'question' : question}
        return render(request, 'pybo/question_detail.html', context)
    except:
        print("error")
        question = []
        context = {'question' : question}
        return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #context={'answer_new' : "fuck"}
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form' : form}
    #return render(request, 'pybo/test.html', context)
    return render(request, 'pybo/question_detail.html', context)

def answer_delete(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        question.delete()    
    return redirect('pybo:index')
    

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})

def board(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/board.html', context)

def timeline(request):
    question_list = Question.objects.order_by('create_date')
    context = {'question_list' : question_list}
    return render(request, "timeline.html", context)