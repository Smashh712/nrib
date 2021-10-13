from django.urls import path
from . import views

app_name = "pybo"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create"),
    path("answer/delete/<int:question_id>/", views.answer_delete, name="answer_delete"),
    path("<int:question_id>/board/", views.board, name="board"),
    path("question/create/", views.question_create, name="question_create"),
    path("test/", views.timeline, name="timeline"),
    path("test2/<issue_id>/", views.discuss, name="discuss"),
    path(
        "issue_reply_create/<issue_id>/<int:_side>/",
        views.issue_reply_create,
        name="issue_reply_create",
    ),
    path(
        "rereply_create/<issue_reply_id>/",
        views.rereply_create,
        name="rereply_create",
    ),
    path("issues/<issue_id>/choice/", views.choice_issue, name="choice_issue"),
]
