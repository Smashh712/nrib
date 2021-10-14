from django.contrib import admin
from .models import Question, Answer, Issue, Issue_reply, Issue_rereply, Topic, Event


class Search_Event(admin.ModelAdmin):
    search_fields = ["subject"]


class Search_Topic(admin.ModelAdmin):
    search_fields = ["subject"]


class Search_Question(admin.ModelAdmin):
    search_fields = ["subject"]


class Search_Answer(admin.ModelAdmin):
    search_fields = ["content"]


class Search_Issue(admin.ModelAdmin):
    search_fields = ["subject"]


class Search_Issue_reply(admin.ModelAdmin):
    search_fields = ["content"]


class Search_Issue_rereply(admin.ModelAdmin):
    search_fields = ["content"]


admin.site.register(Event, Search_Topic)
admin.site.register(Topic, Search_Topic)
admin.site.register(Question, Search_Question)
admin.site.register(Answer, Search_Answer)
admin.site.register(Issue, Search_Issue)
admin.site.register(Issue_reply, Search_Issue_reply)
admin.site.register(Issue_rereply, Search_Issue_rereply)

# Register your models here.
