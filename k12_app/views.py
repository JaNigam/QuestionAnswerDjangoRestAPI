from django.db.models import Max, Q
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from k12_app.models import Question, Answer
from k12_app.serializer import QuestionSerializer, AnswerSerializer, AnswerQuestionSerializer


class QuestionView(ListCreateAPIView):
    """ Question API endpoint """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDetailView(RetrieveAPIView):
    """ Question retrieve API endpoint  """
    serializer_class = AnswerQuestionSerializer
    queryset = Answer.objects.all()


class AnswerView(ListCreateAPIView):
    """ Answer API endpoint"""
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class AnswerDetail(ListAPIView):
    """ Answer list all records  API endpoint """
    serializer_class = AnswerQuestionSerializer
    queryset = Answer.objects.all()


class AnswerupdateDetail(RetrieveUpdateDestroyAPIView):
    """ Answer Retrieve, Update, Destroy API endpoint """
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


@api_view(['GET'])
def get_questions_asked_by_user(request: dict, user_id: int):
    """
    Function to get the asked questions by user

    :param request: request not used
    :param user_id: current user_id
    :return: Serialized data for asked questions of current user
    """
    question_list = Question.objects.filter(user_id=user_id)
    serilizer = QuestionSerializer(question_list, many=True)
    return Response(serilizer.data)


@api_view(['GET'])
def get_answer_given_by_user(request: dict, user_id: int):
    """
    function to get the all questions answer according to user_id

    :param request: not used
    :param user_id: current user_id
    :return: Serialized data to indicate to which questions user gave answer
    """
    answer_list = Answer.objects.filter(user_id=user_id)
    serializer = AnswerSerializer(answer_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_upvote_detail_done_by_user(request, user_id: int):
    """
    function to get records which are upvote by user

    :param request: not used
    :param user_id: current user_id
    :return: Serialized data of upvote records by user
    """
    answer_list = Answer.objects.filter(upvote=user_id)
    serializer = AnswerSerializer(answer_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_max_upvote_ever(request: dict):
    """
    function to get max upvote

    :param request: Not used
    :return: Serialized data of max upvote
    """
    ans = Answer.objects.annotate(upvote_max=Max('upvote')).order_by('-upvote_max')[:1]
    serializer = AnswerSerializer(ans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_max_upvote_by_last_hour(request: dict):
    """
    function to get max upvote in 1 hour

    :param request: Not used
    :return: Serialized data of max upvote in hour
    """
    ans = Answer.objects.annotate(upvote_max=Max('upvote')).filter(Q(create__hour__lt=1)).order_by('-create')
    serializer = AnswerSerializer(ans, many=True)
    return Response(serializer.data)




