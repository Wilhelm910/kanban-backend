from django.db import models
from django.conf import settings
import datetime

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("doing", "Doing"),
        ("review", "Review"),
        ("done", "Done")
    ]
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.date.today)
    checked = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="todo")
    def __str__(self):
        return f'({self.id}) {self.title}'
    


    
