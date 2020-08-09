from django.urls import path
from users.views import UserListView

urlpatterns = [
    path("all/", UserListView.as_view()),
]
