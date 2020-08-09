from django.db import models
from posts.models import User, Post


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,blank=True, editable=False,
                                      verbose_name='Vote')
    user = models.ForeignKey(User, verbose_name='User',
                                   on_delete=models.CASCADE, blank=True, editable=False)
