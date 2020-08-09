from django.urls import path, include
from votes.views import *

urlpatterns = [
    path('vote/<int:user__id>/', VoteView.as_view(), name="test"),
    path('all', VoteListView.as_view()),
]
