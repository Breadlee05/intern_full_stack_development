

from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'user', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['question_text', 'answer_text']
