from django.contrib import admin
from django.urls import path, include
from posts.views import *

urlpatterns = [
    path('post/create', PostCreateView.as_view()),
    path('all', PostListView.as_view()),
    path('post/detail/<int:pk>', PostDetailView.as_view())
]
