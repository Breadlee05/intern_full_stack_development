from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='General')  # Add this line

    def __str__(self):
        return f"{self.user.username}: {self.question_text[:50]}"

    class Meta:
        ordering = ['-created_at']