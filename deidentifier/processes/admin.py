from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(QuestionGroup)
admin.site.register(Question)
admin.site.register(AnswerSet)
admin.site.register(Answer)
