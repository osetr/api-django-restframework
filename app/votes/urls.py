from django.urls import path
from votes.views import VoteListView, VoteView

urlpatterns = [
    path("all/", VoteListView.as_view()),
    path("vote/<int:pk>/", VoteView.as_view()),
]
