from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    goal = models.TextField()
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name

