from django import forms
from pybo.models import Question, Answer, Issue_reply, Issue_rereply


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]
        labels = {
            "subject": "제목",
            "content": "내용",
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {
            "contents": "답변내용",
        }


class Issue_replyForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {
            "contents": "댓글 내용",
        }


class Issue_rereplyForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {
            "contents": "댓글 내용",
        }
