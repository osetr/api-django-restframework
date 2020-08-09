from django.urls import path, include
from users.views import *

urlpatterns = [
    path('all/', UserListView.as_view()),
]
