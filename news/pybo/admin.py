from django.contrib import admin
from .models import Question, Answer

class Search_Question(admin.ModelAdmin):
    search_fields = ['subject']

class Search_Answer(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Question, Search_Question)
admin.site.register(Answer, Search_Answer)


# Register your models here.
