from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue_reply, Issue_rereply, Question, Issue, Topic, Event
from django.utils import timezone
from .forms import QuestionForm, AnswerForm, Issue_rereplyForm, Issue_replyForm
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    page = request.GET.get("page", "1")  # pybo/?page=1 : default=1

    question_list = Issue.objects.order_by("-create_date")

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {"question_list": page_obj}
    return render(request, "pybo/question_list.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        # question = get_object_or_404(Question, pk=question_id)
        context = {"question": question}
        return render(request, "pybo/question_detail.html", context)
    except:
        print("error")
        question = []
        context = {"question": question}
        return render(request, "pybo/question_detail.html", context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # context={'answer_new' : "fuck"}
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("pybo:detail", question_id=question_id)
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    # return render(request, 'pybo/test.html', context)
    return render(request, "pybo/question_detail.html", context)


def answer_delete(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
        question.delete()
    return redirect("pybo:index")


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        form = QuestionForm()
    return render(request, "pybo/question_form.html", {"form": form})


def board(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/board.html", context)


def timeline(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.subject = topic.subject.replace("_", "\n")
    question_list = Event.objects.filter(topic=topic).order_by("create_date")
    start_date = question_list[0].create_date.strftime("%Y.%m.%d")
    end_date = question_list[len(question_list) - 1].create_date.strftime("%Y.%m.%d")
    for i in question_list:
        i.subject = i.subject.replace("_", "\n")
    print()
    context = {
        "question_list": question_list,
        "topic": topic,
        "date": [start_date, end_date],
    }
    return render(request, "timeline.html", context)


def discuss(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    issue_reply = Issue_reply.objects.filter(issue=issue)
    agree_num = issue_reply.filter(side=True).count()
    disagree_num = issue_reply.filter(side=False).count()
    issue_rereply = Issue_rereply.objects
    rereply_num = {}
    for reply in issue_reply:
        i = reply.id
        rereply_num[i] = issue_rereply.filter(issue_reply=i).count()
    context = {
        "issue": issue,
        "num": [agree_num, disagree_num],
        "rereply_num": rereply_num,
    }

    return render(request, "discuss.html", context)


def issue_reply_create(request, issue_id, _side):
    if request.method == "POST":
        issue = get_object_or_404(Issue, pk=issue_id)
        issue.issue_reply_set.create(
            content=request.POST.get("content"),
            create_date=timezone.now(),
            like=0,
            side=_side,
        )
        return redirect("pybo:discuss", issue_id=issue.id)


def rereply_create(request, issue_reply_id):
    if request.method == "POST":
        issue_reply = get_object_or_404(Issue_reply, pk=issue_reply_id)
        issue_reply.issue_rereply_set.create(
            content=request.POST.get("content"),
            create_date=timezone.now(),
            like=0,
        )
        print("test")
        return redirect("pybo:discuss", issue_id=issue_reply.issue.id)


def choice_issue(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.subject = topic.subject.replace("_", "\n")
    issue_list = Issue.objects.filter(topic=topic_id).order_by("create_date")
    reply_num = {}
    sum_reply = 0
    for i in issue_list:
        num = Issue_reply.objects.filter(issue=i).count()
        reply_num[i] = num
        sum_reply += num
    context = {
        "issue_list": issue_list,
        "topic": topic,
        "sum_reply": sum_reply,
        "reply_num": reply_num,
    }
    return render(request, "nrib_choice.html", context)
