from django.contrib.auth.models import User
from rest_framework import serializers

from k12_app.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'user')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer', 'user', 'upvote')


class QuestionSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question',)


class AnswerQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSingleSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('question', 'answer', 'user')


