from django.contrib import admin
from .models import Question,Choice
# Register your models here.

#admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields":["question_text"]}),
        ("Date Information",{"fields":["pub_date"]})
    ]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

