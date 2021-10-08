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
    path("test2/<question_id>/", views.discuss, name="discuss"),
]
