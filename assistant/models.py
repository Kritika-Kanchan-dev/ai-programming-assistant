
from django.db import models

class Chat(models.Model):
    user_prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_prompt[:50]
