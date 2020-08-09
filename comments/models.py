from django.db import models
from posts.models import User, Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,blank=True, editable=False,
                                      verbose_name='Vote')
    author = models.ForeignKey(User, verbose_name='User',
                                   on_delete=models.CASCADE, blank=True, editable=False)
    content = models.CharField(verbose_name='Content', max_length=25)
