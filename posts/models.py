from django.db import models
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()

class Post(models.Model):
    title = models.CharField(verbose_name='Title', max_length=25)
    date = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    author = models.CharField(verbose_name='Author', default="ok", max_length=25)
    upvotes = models.IntegerField(verbose_name='Upvotes', default=0)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
