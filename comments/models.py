from django.db import models
from posts.models import User, Post
from datetime import datetime


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                   editable=False,
                                   verbose_name='Post')
    author = models.ForeignKey(User, verbose_name='Author',
                                     editable=False,
                                     on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Content',
                               max_length=100)
    date = models.DateTimeField(default=datetime.now(),
                                editable=False)

    def __str__(self):
        return '%s commented %s' % (self.author.id, self.post.id)
