from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models he

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=10,
    choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ],
        default='medium'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tasks_details", kwargs={"task_id": self.id})

class Habit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
