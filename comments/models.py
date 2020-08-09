from django.db import models
from posts.models import User, Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, editable=False,
                                      verbose_name='Post')
    author = models.ForeignKey(User, verbose_name='Author',
                                     on_delete=models.CASCADE,
                                     editable=False)
    content = models.CharField(verbose_name='Content', max_length=25)
    # date = models.DateTimeField(auto_now_add=True, editable=False)
