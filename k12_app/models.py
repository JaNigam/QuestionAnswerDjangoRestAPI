from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    """
    Model to store questions

    `question`
        question asked by user

    ``user'
        user id of question asked
    """
    question = models.CharField(max_length=300, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    """
    To store particular questions answer

    `question`
        question instance

    'answer'
        answer of question

    'user'
        link user who gave ans

    'upvote'
        to store upvote for answer from multiple user
        user instance
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote = models.ManyToManyField(User, related_name='upvote', symmetrical=False, null=True, blank=True)
    create = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.question, self.answer, self.user




