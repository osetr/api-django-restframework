from django.urls import path
from comments.views import *

urlpatterns = [
    path("all/", CommentGetAllView.as_view()),
    path("comment/post/<int:pk>/", CommentCreateView.as_view()),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view()),
    path("comment/<int:pk>/", CommentGetView.as_view()),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view()),
]
