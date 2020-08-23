"""k12_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from k12_app.views import (
    QuestionView,
    AnswerView,
    AnswerDetail,
    get_questions_asked_by_user,
    QuestionDetailView,
    get_answer_given_by_user,
    AnswerupdateDetail,
    get_upvote_detail_done_by_user,
    get_max_upvote_ever,
    get_max_upvote_by_last_hour
)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/v1/questions', QuestionView.as_view(), name='question'),
    path('api/v1/question/<int:pk>', QuestionDetailView.as_view()),
    path('api/v1/question_asked_by_user/<int:user_id>', get_questions_asked_by_user),
    path('api/v1/answers', AnswerView.as_view(), name='answer'),
    path('api/v1/answer_given_by_user/<int:user_id>', get_answer_given_by_user),
    path('api/v1/answer/<int:pk>', AnswerupdateDetail.as_view()),
    path('api/v1/my_upvote/<int:user_id>', get_upvote_detail_done_by_user),
    path('api/v1/all_q-a', AnswerDetail.as_view(), name='q-a'),
    path('api/v1/max_vote_ever', get_max_upvote_ever),
    path('api/v1/max_vote_last_hour', get_max_upvote_by_last_hour),
]
