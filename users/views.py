from rest_framework import generics
from users.serializers import UserList
from users.models import User
from rest_framework.permissions import IsAdminUser


class UserListView(generics.ListAPIView):
    serializer_class = UserList
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )
